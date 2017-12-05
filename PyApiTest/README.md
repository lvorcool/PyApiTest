## API接口自动化测试框架
#### 概述   
1. 用python+requests编写接口自动化测试代码,用excel管理接口用例,日常只需将接口测试用例在excel填好,
   代码由Git或Svn管理,配置Jenkins来定期执行脚本获取测试结果
2. 代码结构如下:  
  2.1 .env 是virtualenv创建独立python开发环境,激活用 source .env/bin/active 即可  
  2.2 case文件夹是excel用例模板,结合公司产品填接口信息即可  
  2.3 data文件夹是解决excel数据获取及数据依赖获取  
  2.4 dataconfig是解决cookie数据及请求数据  
  2.5 main文件夹的run_testcase.py是执行接口测试用例,并发测试结果邮件  
  2.6 util是解决excel,json,header的数据获取及写入操作,配置发邮件  
  2.7 base是将requests的get,post二次封装来调用  
3. 使用说明  
  3.1 代码下载到本地只需安装必要的依赖包即可使用  
  3.2 依赖包  
     3.2.1 requests,xlrd,xlutils,jsonpath-rw等  

 