# 2024_POC
poc来自各大威胁情报，进而编写的nuclei模板


常用nuclei 使用命令：
```sh
nuclei -t ./xx.yaml -v -u 192.168.136.130:8080
cat target.txt | nuclei -t ./xx.yaml -v
```


nuclei 自带模板测试：
```sh
nuclei -u https://example.com -tags cve -severity critical,high
```