# 测试阿里千问
#api_key = 'sk-'
#base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
#model  = 'qwen-turbo'
import os
import sys
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(parent_dir)
from GeneralAgent import Agent

#agent = Agent('你是一位资深的AI专家和作家。', model=model, api_key=api_key, base_url=base_url, temperature=0.5, max_tokens=1000, top_p=0.9, frequency_penalty=1)
agent = Agent('你是一位资深的AI专家和杂志编辑。', temperature=0.5, max_tokens=1000, top_p=0.9, frequency_penalty=1)
agent.run(['请你用中文写作。你会仔细阅读参考资料并据此写作一篇内容详实的文章。文笔风趣幽默，突出需要记忆的重点句，并大量使用emoji来表达思想。', {'image': '../docs/images/self_call.png'}], display=True)