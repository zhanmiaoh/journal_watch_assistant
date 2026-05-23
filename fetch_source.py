import requests
import re
from urllib.parse import unquote

import html
from bs4 import BeautifulSoup

def get_full_abstract_from_crossref(doi):
    """通过 DOI 从 Crossref 获取完整的摘要"""
    url = f"https://api.crossref.org/works/{doi}"
    try:
        # Crossref 建议在 headers 里加上你的邮箱，这样属于 "Polite" 爬虫，不容易被封
        headers = {'User-Agent': 'mailto:zhuangdj@connect.ust.hk'}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Crossref 的摘要通常带有 HTML 标签，比如 <jats:p>
            abstract = data['message'].get('abstract', '')
            return abstract
    except Exception as e:
        print(f"Crossref fetch failed: {e}")
    return None


def get_full_text_from_pmc(doi):
    # Europe PMC 的全文本 XML 接口
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&resultType=core&format=json"
    
    try:
        response = requests.get(url).json()
        results = response.get('resultList', {}).get('result', [])
        
        if not results:
            return None, "未在 PMC 找到该文章"
            
        article_data = results[0]
        
        # 检查是否有开源的全文本 (Open Access)
        if article_data.get('isOpenAccess') == 'Y' and article_data.get('hasTextMinedTerms') == 'Y':
            # 获取 XML 下载链接
            pmcid = article_data.get('pmcid')
            xml_url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
            xml_content = requests.get(xml_url).text
            return xml_content, "成功获取全文本 XML"
        else:
            return None, "该文章不是 Open Access，或者 PMC 尚未解析全文"
            
    except Exception as e:
        return None, str(e)


def extract_doi(entry):
    """
    【终极补丁版】从 RSS entry 中极其稳健地提取 DOI。
    完美兼容 bioRxiv 版本号以及 Nature 家族无 10.1038 前缀的隐藏 URL。
    """
    doi_pattern = r"(10\.\d{4,9}/[^\s?#]+)"
    
    # 【第一步】：优先检查 RSS 的专属标识符字段 (id, guid)
    for field in ['id', 'guid', 'dc_identifier']:
        identifier = entry.get(field, "")
        if identifier and "10." in identifier:
            match = re.search(doi_pattern, identifier)
            if match:
                return match.group(1).rstrip('.)]')

    # 【第二步】：从 URL (link) 中强行正则提取
    link = entry.get("link", "")
    if not link:
        return None
        
    decoded_link = unquote(link)
    
    # 核心硬核修复：针对 Nature 家族期刊 URL 的特殊打补丁逻辑
    if "nature.com/articles/" in decoded_link.lower():
        # 提取 articles/ 后面的核心字符串 (例如 s41467-026-73057-5)
        nature_match = re.search(r"articles/([^\s?#]+)", decoded_link)
        if nature_match:
            # 强行在前端拼接 Nature 家族在 Crossref 上的专属注册码 10.1038/
            nature_doi = f"10.1038/{nature_match.group(1)}"
            return nature_doi.rstrip('.)]')

    # 【第三步】：走通用的标准 DOI 提取逻辑
    match = re.search(doi_pattern, decoded_link)
    if match:
        doi = match.group(1).rstrip('.)]')
        
        # 清除 bioRxiv 链接自带的版本号后缀 (如 v1, v2)
        if "biorxiv.org" in link.lower() and re.search(r'v\d+$', doi):
            doi = re.sub(r'v\d+$', '', doi)
            
        return doi

    # 如果所有方法都失效，返回 None
    return None


def clean_html_tags(raw_text):
    """
    清除文本中的 HTML/XML 标签，并处理特殊转义字符。
    适用于清洗 Crossref 或 PMC 返回的带有复杂标签的学术摘要。
    """
    if not raw_text:
        return ""
    
    # 1. 解码 HTML 实体
    # 将 &amp; 还原为 &, &#39; 还原为 '，避免被当作无意义字符
    unescaped_text = html.unescape(raw_text)
    
    # 2. 使用 BeautifulSoup 剥离所有标签
    # 关键参数 separator=" ": 确保 <p>段落A</p><p>段落B</p> 被剥离后，
    # 中间会插入空格，防止变成 "段落A段落B"
    try:
        soup = BeautifulSoup(unescaped_text, "html.parser")
        text_only = soup.get_text(separator=" ", strip=True)
    except Exception as e:
        print(f"  [警告] BeautifulSoup 解析异常，回退到正则清洗: {e}")
        # 极小概率发生异常时的防崩溃降级方案
        text_only = re.sub(r'<[^>]+>', ' ', unescaped_text)
    
    # 3. 清理多余的空白字符
    # 将连续的多个空格、换行符、制表符压缩为一个单一空格
    clean_text = re.sub(r'\s+', ' ', text_only).strip()
    
    return clean_text

# --- 测试用例 ---
# 模拟 Crossref 返回的典型脏数据
# sample_abstract = "<jats:title>Abstract</jats:title><jats:p>The PFC controls timing.</jats:p><jats:p>It uses <i>ramping</i> &amp; dynamics.</jats:p>"
# print(clean_html_tags(sample_abstract))
# 期望输出: "Abstract The PFC controls timing. It uses ramping & dynamics."


# --- 在你的主循环里这样用 ---
# if __name__ == "__main__":
#     for entry in entries:
#         title = entry.get("title", "")
#         rss_abstract = entry.get("summary", "")
#         link = entry.get("link", "")
        
#         # 1. 尝试从链接中提取 DOI (PNAS 的链接通常是 https://www.pnas.org/doi/10.1073/pnas...)
#         doi = extract_doi_from_link(link) 
        
#         # 2. 判断 RSS 摘要是否被恶意截断 (比如包含 ... 或长度过短)
#         if "..." in rss_abstract[-10:] or len(rss_abstract) < 400:
#             print(f"  [发现截断] 正在通过 Crossref 补全摘要: {title[:30]}...")
#             full_abstract = get_full_abstract_from_crossref(doi)
            
#             # 如果成功抓到了完整的，就替换掉残缺的 RSS 摘要
#             if full_abstract:
#                 rss_abstract = clean_html_tags(full_abstract) 
        
#         # 3. 再把完整拼接的文本喂给大模型进行 Relevance 判定
#         report = analyze_paper(title, rss_abstract, link, journal, ...)
