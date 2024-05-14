# 2024_POC
poc从各大威胁情报、github、csdn、个人复现等途径中获取

编写的nuclei模板特点：
- 精心编写，均为nuclei-templates 项目中没有的模板
- 点到即止，测试链无害、无痕
- 包含热门管理系统厂商用友等
- ~~无0day~~

常用nuclei 使用命令：
```sh
nuclei -t ./xx.yaml -v -u 192.168.136.130:8080
cat target.txt | nuclei -t ./xx.yaml -v
```


nuclei 自带模板测试：
```sh
nuclei -u https://example.com -tags cve -severity critical,high
```