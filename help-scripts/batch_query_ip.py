import os
import re
import requests

# 定义要遍历的目录
directory = './path/to/your/directory'  # 替换为你的目录路径

# 定义正则表达式来匹配特定的字符串模式
pattern = re.compile(
    r'Details: \*\*2024-105272020\*\* matched at (\d+\.\d+\.\d+\.\d+:\d+)'
)

# 定义API的URL（替换为你的API地址）
api_url = 'https://example.com/api/query'  # 替换为你的API地址

# 定义输出文件
output_file = 'output.txt'

# 打开输出文件
with open(output_file, 'w') as outfile:
    # 遍历指定目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理.md结尾的文件
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    # 查找匹配的字符串
                    matches = pattern.findall(content)
                    for match in matches:
                        # 调用API进行查询
                        response = requests.get(api_url, params={'query': match})
                        if response.status_code == 200:
                            data = response.json().get('data', '')
                            # 将返回的data字段写入输出文件
                            outfile.write(f'{match}: {data}\n')
                        else:
                            print(
                                f'API调用失败: {response.status_code}, {response.text}'
                            )
