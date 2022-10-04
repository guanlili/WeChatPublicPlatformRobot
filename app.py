# -*- coding:utf-8 -*-
from flask import Flask
from flask import request
import time
import SelectStudent
import xml.etree.ElementTree as ET
import hashlib
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello World!"
@app.route("/wechat", methods=["GET","POST"])
def weixin():
    if request.method == "GET":     # 判断请求方式是GET请求
        my_signature = request.args.get('signature')     # 获取携带的signature参数
        my_timestamp = request.args.get('timestamp')     # 获取携带的timestamp参数
        my_nonce = request.args.get('nonce')        # 获取携带的nonce参数
        my_echostr = request.args.get('echostr')         # 获取携带的echostr参数
        token = "qazqaz1921"  # 一定要跟刚刚填写的token一致
        # 进行字典排序
        data = [token, my_timestamp, my_nonce]
        data.sort()
        # 拼接成字符串，进行hash加密时需要为字符串类型
        temp = ''.join(data)
        # 创建一个hash对象
        s = hashlib.sha1()
        # 对创建的hash对象更新需要加密的字符串
        s.update(temp.encode("utf-8"))
        # 加密处理
        mysignature = s.hexdigest()
        print("handle/GET func: mysignature, my_signature: ", mysignature, my_signature)
        # 加密后的字符串可与signature对比，标识该请求来源于微信
        if my_signature == mysignature:
            return my_echostr
        else:
            return ""
    else:
        # 解析xml
        xml = ET.fromstring(request.data)
        print("xml=",xml)
        toUser = xml.find('ToUserName').text
        print("toUser=", toUser)
        fromUser = xml.find('FromUserName').text
        print("fromUser=", fromUser)
        msgType = xml.find("MsgType").text
        print("msgType=", msgType)
        createTime = xml.find("CreateTime")
        print("createTime=", createTime)

        # 判断类型并回复
        if msgType == "text":
            content = xml.find('Content').text
            print("content=",content)
            # return reply_text(fromUser, toUser, "我只懂文字1")
            if "谢谢" in content or "感谢" in content:
                return reply_text(fromUser, toUser, "不客气哦，这是我应该做的/爱心")
            if "航旅" in content or "航旅纵横" in content or "内推" in content:
                return reply_text(fromUser, toUser, "内推群请添加微信：outman_1921，我拉你进群")
            return reply_text(fromUser, toUser, SelectStudent.excel_reply(content))


            # return reply_text(fromUser, toUser, "您查找的候选人不存在")
        elif msgType == "event":
            Event = xml.find('Event').text
            if Event == "subscribe":
                subscribe_reply = "欢迎关注李梨同学\n" \
                                  "这里可以进行航旅纵横校招内推\n" \
                                  "也会分享学习工作中的心得体会\n"\
                                  "期待与你共同成长/爱心\n"
                return reply_text(fromUser, toUser, subscribe_reply)


        else:
            return reply_text(fromUser, toUser, "李梨同学目前只能接收文字哦")
        pass


def reply_text(to_user, from_user, content):
    """
    以文本类型的方式回复请求
    """
    return """
    <xml>
        <ToUserName><![CDATA[{}]]></ToUserName>
        <FromUserName><![CDATA[{}]]></FromUserName>
        <CreateTime>{}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{}]]></Content>
    </xml>
    """.format(to_user, from_user, int(time.time() * 1000), content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)