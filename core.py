#!/usr/bin/python2
# coding:utf8
""" 校园网登录 """
''' http://login.ecust.edu.cn '''


# import _elementpath as DONTUSE


def login_ecust_net(stu_id, stu_pw):
    import re
    import requests
    from lxml import etree

    # valid
    if "http-equiv='refresh'" in requests.get("http://www.baidu.com").text:
        pass
    else:
        return 0
    req = requests.Session()
    req.trust_env = False
    first_req = req.get('http://login.ecust.edu.cn')
    second_url = re.compile('http://login.ecust.edu.cn/&arubalp=.*\'').findall(first_req.text)[0][:-1]
    second_req = req.get(second_url)
    ac_id = re.compile("/index_([\d]+).html").findall(second_req.url)[0]
    # print second_req.url
    args = re.compile('cmd=login.*&url=http%3A%2F%2Flogin.ecust.edu.cn%2F').findall(second_req.url)[0]
    location = re.compile('http://[0-9]*.[0-9]*.[0-9]*.[0-9]*/').findall(second_req.url)[0]
    third_url = location + "ac_detect.php?" + "ac_id=" + ac_id + "&" + args
    third_req = req.get(third_url)
    final_url = third_req.url
    html = etree.HTML(third_req.text)
    data = {"action": html.xpath("//input[@name='action']")[0].attrib['value'],
            "ac_id": html.xpath("//input[@name='ac_id']")[0].attrib['value'],
            "user_ip": html.xpath("//input[@name='user_ip']")[0].attrib['value'],
            "nas_ip": html.xpath("//input[@name='nas_ip']")[0].attrib['value'],
            "user_mac": html.xpath("//input[@name='user_mac']")[0].attrib['value'],
            "url": html.xpath("//input[@name='url']")[0].attrib['value'],
            "ip": html.xpath("//input[@name='ip']")[0].attrib['value'], "username": str(stu_id) + "@free",
            "password": stu_pw, "ajax": "1"}
    # data["opt"] = "@free" # 免费value为@free，非免费为空
    final_req = req.post(final_url, data=data)
    if "login_ok" in final_req.text:
        return req.cookies  # 虽然我也不知道这个Cookie有啥用
    else:
        return False


if __name__ == '__main__':
    import os

    # print StuID, StuPW
    if os.path.exists("conf"):
        # getConf()
        conf = open("conf", "r").readlines()
        StuID = conf[0]
        StuPW = conf[1]
    else:
        StuID = raw_input("输入学号 Input your StudentID :")
        StuPW = raw_input("输入密码 Input your StudentPW :")
        conf = open("conf", "w+")
        conf.write(StuID + "\n")
        conf.write(StuPW + "\n")
    # print "SID =" + StuID + "SPW =" + StuPW
    if login_ecust_net(StuID, StuPW) is False:
        # 返回一个Cookie对象即成功，否则失败。
        print("失败 Failed")
    elif login_ecust_net(StuID, StuPW) is 0:
        print("已在能联网环境 Connected")
    else:
        print("成功 Success")
