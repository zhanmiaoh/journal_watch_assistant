import datetime
import os
import requests
import feedparser
import time
from openai import OpenAI
from dotenv import load_dotenv

from rss_sources import TEST_RSS_FEEDS as RSS_FEEDS
from system_prompt import PRE_FILTER_KEYWORDS, SYSTEM_PROMPT
from fetch_source import get_full_abstract_from_crossref, get_full_text_from_pmc, extract_doi


# ==========================================
# 1. API Client & 日期设定
# ==========================================
ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=ENV_PATH, override=False)

API_KEY = os.getenv("API_KEY", "")
BASE_URL = os.getenv("BASE_URL", "https://api.deepseek.com")
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-v4-flash")
TIMEOUT_SECONDS = int(os.getenv("TIMEOUT_SECONDS", "120"))

client = OpenAI(api_key=API_KEY, base_url=BASE_URL, timeout=TIMEOUT_SECONDS)

# # Gemini API Key (可在 Google AI Studio 获取免费 API)
# import google.generativeai as genai
# GEMINI_API_KEY = ""
# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel('gemini-1.5-pro')
# prompt = f"{SYSTEM_PROMPT}\n\nJournal: {journal}\nPaper Title: {title}\nAbstract: {abstract}\nURL: {url}"
# response = model.generate_content(prompt)
# text = response.text.strip()


# 设置 BioRxiv 检索的日期范围 (动态获取本月 11号 - 20号)
today = datetime.date.today()
START_DATE = today.replace(day = 11).strftime("%Y-%m-%d")
END_DATE = today.replace(day = 20).strftime("%Y-%m-%d")
# START_DATE = datetime.date(2026, 4, 11)
# END_DATE = datetime.date(2026, 4, 20)

# 二选一：Journal RSS 日期过滤选项 / 每期刊最新 20 篇 
RSS_USE_DATE_RANGE = False  # False: 用最新 20 篇
# True: 用日期区间
# RSS_START_DATE = datetime.date(2026, 4, 1)
# RSS_END_DATE = datetime.date(2026, 5, 20)
# RSS_END_DATE = today
# RSS_START_DATE = today - datetime.timedelta(days=7)  # 默认最近一周内的文章
# _this_monday = today - datetime.timedelta(days=today.weekday())
# RSS_START_DATE = _this_monday - datetime.timedelta(days=7)


# ==========================================
# 2. Prompt 设定 (has been imported from system_prompt.py)
# ==========================================


# ==========================================
# 3. 抓取与分析逻辑
# ==========================================
def analyze_paper(title, abstract, url, journal, authors, affiliations, full_text_xml, log_call):
    user_content = (
        f"Journal: {journal}\n"
        f"Paper Title: {title}\n"
        f"Authors: {authors}\n"
        f"Affiliations: {affiliations}\n"
        f"Abstract: {abstract}\n"
        f"Full Text XML: {full_text_xml}\n"
        f"URL: {url}"
    )
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_content}
            ],
            max_tokens=4096,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
        )
        
        content = response.choices[0].message.content or ""
        reasoning_content = getattr(response.choices[0].message, "reasoning_content", "") or ""
        log_call(journal, title, user_content, content, reasoning_content)

        text = content.strip()
        
        # 截断处理：如果不相关，模型应该只返回 NOT_RELEVANT
        if text == "NOT_RELEVANT" or "NOT_RELEVANT" in text:
            return None
            
        return text
    
    except Exception as e:
        print(f"API Error processing {title}: {e}")
        time.sleep(5)  # 简单的错误重试缓冲
        return None

def fetch_biorxiv(write_report, log_call):
    print(f"[*] Fetching BioRxiv papers from {START_DATE} to {END_DATE}...")
    report_count = 0
    cursor = 0
    while True:
        url = f"https://api.biorxiv.org/details/biorxiv/{START_DATE}/{END_DATE}/{cursor}"
        try:
            res = requests.get(url).json()
            collection = res.get("collection", [])
            if not collection:
                break
            
            for paper in collection:
                if paper.get("category", "").lower() != "neuroscience":
                    continue
                
                title = paper.get("title", "")
                abstract = paper.get("abstract", "")
                
                combined_text = (title + " " + abstract).lower()
                target_kws = ["network", "circuit", "theory", "dynamics"]
                if any(kw in combined_text for kw in target_kws):
                    print(f"  [BioRxiv candidate found] {title[:60]}...")
                    
                    authors_raw = paper.get("authors", "") or ""
                    first_author = authors_raw.split(";")[0].strip() if authors_raw else "Unknown"
                    corr_author = paper.get("author_corresponding", "") or "Unknown"
                    corr_inst = paper.get("author_corresponding_institution", "") or "Unknown"
                    authors = f"First Author: {first_author} | Corresponding: {corr_author}"
                    affiliations = f"Corresponding Inst: {corr_inst}"

                    report = analyze_paper(
                        title,
                        abstract,
                        f"https://doi.org/{paper.get('doi')}",
                        "BioRxiv",
                        authors,
                        affiliations,
                        None,
                        log_call
                    )
                    if report:
                        write_report(report)
                        report_count += 1
            
            cursor += 100
        except Exception as e:
            print(f"Error fetching BioRxiv API: {e}")
            break
            
    return report_count

def fetch_rss_journals(write_report, log_call):
    report_count = 0
    for journal, feed_url in RSS_FEEDS.items():
        print(f"[*] Fetching RSS for {journal}...")
        feed = feedparser.parse(feed_url)
        if RSS_USE_DATE_RANGE:
            def entry_in_range(entry):
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    published = entry.published_parsed
                elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                    published = entry.updated_parsed
                else:
                    return False
                entry_date = datetime.date(published.tm_year, published.tm_mon, published.tm_mday)
                return RSS_START_DATE <= entry_date <= RSS_END_DATE

            entries = [e for e in feed.entries if entry_in_range(e)]
        else:
            entries = feed.entries[:20]  # 每个期刊检查最新的 20 篇

        for entry in entries:
            title = entry.get("title", "")
            rss_abstract = entry.get("summary", "")
            link = entry.get("link", "")
            doi = extract_doi(entry)
            if not doi:
                print(f"  [DOI Extraction Failed] 请检查{journal}的 RSS 格式: {link}")
            # else:
                # 触发后续的 Crossref 或 Europe PMC 逻辑...
            
            # 1. 首先用 crossref 补全摘要（如果 RSS 摘要过短或被截断）
            if "..." in rss_abstract[-10:] or len(rss_abstract) < 400:
                print(f"  [Completing abstract truncation via Crossref]: {title[:30]}...")
                full_abstract = get_full_abstract_from_crossref(doi)
                # 如果成功抓到了完整的，就替换掉残缺的 RSS 摘要
                if full_abstract:
                    rss_abstract = full_abstract

            combined_text = (title + " " + rss_abstract).lower()
            if not any(kw in combined_text for kw in PRE_FILTER_KEYWORDS):
                continue

            print(f"  [{journal} candidate found] {title[:60]}...")
            authors_raw = entry.get("author", "") or ""
            first_author = authors_raw.split(";")[0].strip() if authors_raw else "Unknown"
            affiliations = "Affiliations not available in RSS feed"

            # 2. 尝试用 Europe PMC：获取全文
            # full_text_xml, status_msg = get_full_text_from_pmc(doi)
            # print(f"{status_msg}")
            # 先不获取全文，等模型确认相关性后再补全全文进行二次分析（如果需要）
            full_text_xml = None  
            report = analyze_paper(
                title,
                rss_abstract,
                link,
                journal,
                first_author,
                affiliations,
                full_text_xml, # None, or full text
                log_call
            )
        
            if report:
                write_report(report)
                report_count += 1
    return report_count

# ==========================================
# 4. 主函数与文件生成
# ==========================================
def main():
    print("🚀 Starting Automated Literature Briefing Pipeline...")
    filename = f"Journal_Watch_Report_{today.strftime('%Y-%m-%d')}.md"
    log_filename = f"logs/api_log_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')}.txt"
    report_count = 0
    log_count = 0
    with open(filename, "w", encoding="utf-8") as f, open(log_filename, "w", encoding="utf-8") as log_f:
        f.write(f"# 🧪 组会前沿文献简报 ({today.strftime('%Y-%m-%d')})\n\n")
        f.write(f"- RSS journals: {', '.join(RSS_FEEDS.keys())}\n")
        if RSS_USE_DATE_RANGE:
            f.write(f"- RSS date range: {RSS_START_DATE} to {RSS_END_DATE}\n")
        else:
            f.write("- RSS date range: latest 20 entries per journal\n")
        f.write(f"- BioRxiv date range: {START_DATE} to {END_DATE}\n\n---\n\n")
        f.flush()

        def log_call(journal, title, user_content, content, reasoning_content):
            nonlocal log_count
            log_count += 1
            log_f.write(f"{log_count}. [{journal}] {title}\n")
            log_f.write("USER_PROMPT:\n")
            log_f.write(user_content)
            log_f.write("\n\n")
            log_f.write("REASONING_CONTENT:\n")
            log_f.write(reasoning_content)
            log_f.write("\n\nCONTENT:\n")
            log_f.write(content)
            log_f.write("\n\n---\n\n")
            log_f.flush()

        def write_report(report_text):
            nonlocal report_count
            if report_count > 0:
                f.write("\n\n---\n\n")
            lines = report_text.splitlines()
            for i, line in enumerate(lines):
                if line.startswith("### 📌"):
                    lines[i] = line.replace("### 📌", f"### {report_count + 1}. 📌", 1)
                    break
            else:
                lines.insert(0, f"### {report_count + 1}.")
            f.write("\n".join(lines))
            f.flush()
            report_count += 1

        fetch_biorxiv(write_report, log_call)
        fetch_rss_journals(write_report, log_call)

    if report_count == 0:
        print("No highly relevant papers found today.")
        return

    print(f"✅ Success! Report generated: {filename}")

if __name__ == "__main__":
    main()