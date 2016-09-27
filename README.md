# Project EcustNet

### 简介 · Introduction

本项目唯一目的为服务学在华理的各位。

EcustNet为华理校园网（“ECUST”）的**自动连接程序**。

### 版本 · Version  

#### 1. Python(命令行)：run.py

使用方法：

1. 编辑run.py内学号信息

2. 然后日常需要连接校园网时，命令行中`python run.py`即可

#### 2. NodeJS(命令行):JS_version/app.js

使用方法:

1. `npm install cheerio`

2. app.js对应处填写学号密码

3. `node app.js`

### 待办 · TODO

1. 完善命令行版本

2. 适配Jython，方便日后Jython for android **OR** 直接做个Java版本

3. 写个Swift版本方便各位iOS开发

4. 感谢cordova-plugin-http，这样会点JS的我也能写这个的APP了吧 ……

### QQ群 · QQ Group

本项目极度缺人（尤其Android&iOS），欢迎加入本项目，QQ群:56083540

### 日志 · Log
2016年 09月 27日 星期二 22:37:40 CST

	完成cordova-plugin-http的测试（可在Cordova5.4.0下运行，Cordova6.*迷之闪退）。

	成功重写出NodeJS版本，可日后进行函数替换成为浏览器版方便嵌入Cordova。

	听说徐汇已经实现无线感知了（即服务器端识别设备）。
