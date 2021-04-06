# SearchCodeSpider
企业源码泄露自检脚本\源码泄露检测脚本

### 开发语言：
python

### 工具原理：
https://searchcode.com/
根据关键字在上述站点的检索结果，使用python爬虫将包含关键字的url连接爬取下来，并以每个关键字作为文件名称分别保存到txt文件中


### 使用方法：
1.keyword.txt文件内添加关键字

2.执行py脚本（执行前需安装所需库文件）

3.结果自动生成文本文件，如果检测结果为空则不生成



结果如图：

爬取的链接均为包含关键字的链接

![image-20210406190143186](https://raw.githubusercontent.com/heriachen/cloudimg/main/img2/image-20210406190143186.png)