import time


RSS_PREFILTER_SYSTEM_PROMPT = """
You are a principal investigator and expert in Computational Neuroscience. Your task is to review a newly published paper and determine if it strictly matches the research interests of specific lab members.

### Lab Members & Topics:
- **Zixiang**: task-performing RNN, recurrent models of working memory, cognitive tasks and neural dynamics (eg. ramping activity, decaying activity) on mice experiments or models, methods of inferring effective connectivity, foundation model of neural data.
- **Zhanmiao**: Biological plausible learning, alternative to backpropagation, biological reinforcement learning, LLM application in neuroscience.
- **Xuanyu**: Approximation theory for learning DS trajectories with NN.
- **Whole lab**: Fundamental theories of neural network dynamics, correlations, dimensionality, impact of connectivity, motifs.
- PS: We mainly focus on computational neuroscience papers, but: If the tasks and results in experimental papers are relevant/potentially useful to lab's models (eg. cortical ramping/decaying neural dynamics for RNN) even though it does not incorporate models, or If an experimental paper has strong computational/theoretical component that is highly relevant to the lab's interests, then it should be considered relevant. If the paper is purely experimental without potential applications to our models, it is likely not relevant.  (ps: We are not interested in RNA.)


### Task:
1. Read the Paper Title, Abstract provided by the user.
2. If the paper is clearly irrelevant with ANY of the specific topics above, respond with EXACTLY: NOT_RELEVANT
3. If it might be relevant and needs full-text review, respond with EXACTLY: POSSIBLY_RELEVANT

Return only one of the two tokens above.
"""


def prefilter_rss_relevance(client, model_name, title, abstract, url, journal):
	user_content = (
		f"Journal: {journal}\n"
		f"Paper Title: {title}\n"
		f"Abstract: {abstract}\n"
		f"URL: {url}"
	)

	try:
		response = client.chat.completions.create(
			model=model_name,
			messages=[
				{"role": "system", "content": RSS_PREFILTER_SYSTEM_PROMPT},
				{"role": "user", "content": user_content}
			],
			max_tokens=16,
			reasoning_effort="high",
			extra_body={"thinking": {"type": "enabled"}}
		)

		content = response.choices[0].message.content or ""
		reasoning = getattr(response.choices[0].message, "reasoning_content", "") or ""
		decision = (content or reasoning).strip()
		return decision, content, reasoning
	except Exception as e:
		print(f"RSS prefilter error for {title}: {e}")
		time.sleep(2)
		return "ERROR", "", ""


# 日期过滤逻辑示例（以 11日-20日 为例）
# from datetime import datetime

# for entry in feed.entries:
#     # 拿到文章发布的具体日子 (day)
#     # bioRxiv 的 entry 通常包含 published_parsed 或 updated_parsed 结构
#     if hasattr(entry, 'published_parsed'):
#         pub_day = entry.published_parsed.tm_mday
        
#         if 11 <= pub_day <= 20:
#             # 满足日期，送给 Kimi/DeepSeek 总结
#             pass