import re
import requests
import os

cur = os.path.dirname(__file__)
# 定义输入文本
with open(
    os.path.join(cur, 'results.txt'), 'r', encoding='utf-8', errors='ignore'
) as file:
    input_text = file.read()

# 使用正则表达式提取 URL
urls = input_text.split('\n')
print(urls)

# 输出文件路径
output_file_path = os.path.join(cur, 'output.txt')

# 打开文件以写入
with open(output_file_path, 'w', encoding='utf-8') as file:
    for url in urls:
        try:
            # 发送 HTTP GET 请求
            response = requests.get(url)
            # 写入响应内容
            file.write(f"URL: {url}\n")
            file.write("Response:\n")
            file.write(response.text)
            file.write("\n---END OF RESPONSE---\n\n")
        except requests.exceptions.RequestException as e:
            # 打印出现的异常
            file.write(f"Error accessing {url}: {str(e)}\n")
            file.write("\n---END OF ERROR---\n\n")

print("URLs have been processed and the results are saved in 'output.txt'.")
