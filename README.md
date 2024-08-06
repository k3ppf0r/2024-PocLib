# 2024-PocLib
本项目主要目的是为供个人研究存档使用，也能为网络安全爱好者们提供一点参考资料，共勉

## 漏洞汇总
- 同享TXEHR V15人力管理管理平台strCardNo存在SQL注入漏洞
- 契约锁电子签章平台 param-edits 远程代码执行漏洞
- Apache OFBiz 授权不当致远程代码执行漏洞(CVE-2024-38856)

## poc来源
- 各大威胁情报 
- github
- 博客网站 csdn、cnsec
- 个人复现

## 项目特点
- poc武器化, 开箱即用，所有poc已自测通过
- 精心编写，大多为国有软件相关漏洞,包含热门管理系统厂商用友等, 绝大部分是 nuclei-templates 项目中没有的模板
- 点到即止，测试链无害、无痕
- nuclei_templates目录下存放通用nuclei模板
- xray_templates目录下存放通用xray模板
- help-scripts目录下存放辅助py脚本(如本地开启简易漏洞环境)


## 使用方法
常用nuclei 使用命令：
```sh
nuclei -t ./xx.yaml -v -u 192.168.136.130:8080
# 批量
cat target.txt | nuclei -t ./xx.yaml -v
```

常用xray 使用命令：
```sh
.\xray_windows_amd64.exe ws --poc .\xxx.yml --url https://example.com 
# 批量
.\xray_windows_amd64.exe ws --poc .\xxx.yml --uf .\uf.txt
```

nuclei 自带模板测试：
```sh
nuclei -u https://example.com -tags cve -severity critical,high
```

## 成功截图
某个poc nuclei 演示:

![](https://github.com/k3ppf0r/2024_POC/blob/main/2024-5-17/2024%E7%94%A8%E5%8F%8Bpoc/%E7%94%A8%E5%8F%8BU8CRM%E5%AE%A2%E6%88%B7%E5%85%B3%E7%B3%BB%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9Fdownloadfile.php%E5%AD%98%E5%9C%A8%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E/image.png "攻击演示")

xray 演示:
![](https://github.com/k3ppf0r/2024_POC/blob/main/2024-8-xray/%e5%90%8c%e4%ba%ab%54%58%45%48%52%20%56%31%35%e4%ba%ba%e5%8a%9b%e7%ae%a1%e7%90%86%e7%ae%a1%e7%90%86%e5%b9%b3%e5%8f%b0%73%74%72%43%61%72%64%4e%6f%e5%ad%98%e5%9c%a8%53%51%4c%e6%b3%a8%e5%85%a5%e6%bc%8f%e6%b4%9e/image.png "攻击演示2")


# 免责声明
由于传播、利用本文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责。未经授权对目标进行渗透测试是违法的，并且可能导致严重的法律后果。如发生违法犯罪行为，非授权攻击行为于本项目无关。
