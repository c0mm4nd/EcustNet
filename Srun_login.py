#!/usr/bin/python2
# coding:utf8
''' 校园网登录 '''
''' http://login.ecust.edu.cn '''
import requests
import re
from lxml import etree
def Login(stuID, stuPW):
    # valid
    if "http-equiv='refresh'" in requests.get("http://www.baidu.com").text :
        pass
    else:
        exit()
    req = requests.Session()
    firstReq = req.get('http://login.ecust.edu.cn')
    secondUrl = re.compile('http://login.ecust.edu.cn/&arubalp=.*\'').findall(firstReq.text)[0][:-1]
    secondReq = req.get(secondUrl)
    acId = re.compile("/index_([\d]+).html").findall(secondReq.url)[0]
    print secondReq.url
    args = re.compile('cmd=login.*&url=http%3A%2F%2Flogin.ecust.edu.cn%2F').findall(secondReq.url)[0]
    location = re.compile('http://[0-9]*.[0-9]*.[0-9]*.[0-9]*/').findall(secondReq.url)[0]
    thirdUrl =location + "ac_detect.php?" + "ac_id="+ acId + "&" + args
    thirdReq = req.get(thirdUrl)
    finalUrl = thirdReq.url
    html = etree.HTML(thirdReq.text)
    stuID = 10142045
    stuPW = 951120
    data = {}
    data["action"] = html.xpath("//input[@name='action']")[0].attrib['value']
    data["ac_id"] = html.xpath("//input[@name='ac_id']")[0].attrib['value']
    data["user_ip"] = html.xpath("//input[@name='user_ip']")[0].attrib['value']
    data["nas_ip"] = html.xpath("//input[@name='nas_ip']")[0].attrib['value']
    data["user_mac"] = html.xpath("//input[@name='user_mac']")[0].attrib['value']
    data["url"] = html.xpath("//input[@name='url']")[0].attrib['value']
    data["ip"] = html.xpath("//input[@name='ip']")[0].attrib['value']
    # data["opt"] = "@free" # 免费value为@free，非免费为空
    data["username"] = str(stuID) + "@free" #学号
    data["password"] = stuPW
    data["ajax"] = "1"
    finalReq = req.post(finalUrl, data=data)
    if "login_ok" in finalReq.text:
        return req.cookies #虽然我也不知道这个Cookie有啥用
    else:
        return False
