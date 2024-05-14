import re

# 匹配一个特定的文件名
filename = "example.txt"
pattern = re.compile("example\\.txt")

# 搜索文件名
match = pattern.search(filename)
if match:
    print("Match found")
else:
    print("No match")
