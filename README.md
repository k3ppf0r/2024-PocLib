# 2024_POC
本项目旨在为网络安全爱好者们提供一点参考资料，共勉

## poc来源
- 各大威胁情报 
- github
- 博客网站 csdn、cnsec
- 个人复现

## nuclei模板特点
- 精心编写，均为nuclei-templates 项目中没有的模板
- 点到即止，测试链无害、无痕
- 包含热门管理系统厂商用友等
- ~~无0day~~

## 使用方法
常用nuclei 使用命令：
```sh
nuclei -t ./xx.yaml -v -u 192.168.136.130:8080
cat target.txt | nuclei -t ./xx.yaml -v
```


nuclei 自带模板测试：
```sh
nuclei -u https://example.com -tags cve -severity critical,high
```

## 成功截图
poc演示

![](https://github.com/k3ppf0r/2024_POC/blob/main/2024-5-17/2024%E7%94%A8%E5%8F%8Bpoc/%E7%94%A8%E5%8F%8BU8CRM%E5%AE%A2%E6%88%B7%E5%85%B3%E7%B3%BB%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9Fdownloadfile.php%E5%AD%98%E5%9C%A8%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E6%BC%8F%E6%B4%9E/image.png "攻击演示")