# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
from tmp import novel

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "maoshen1" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is:  ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    print 'The user message(5.26):---',recMsg.Content,'---'
                    head=recMsg.Content.split('.')[0]
                    page=recMsg.Content.split('.')[1]
                    if head=='king':
                        print '>>>',head,page
                         a= novel.Choose(head,page)
                        content=a.decode('unicode-escape').encode('utf-8')
                    elif recMsg.Content=='fuck':
                        content = u"尚未完成".encode('utf-8')
                    else:
                        content = "come on babby"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
            if isinstance(recMsg, receive.EventMsg):
                if recMsg.Event == 'CLICK':
                    if recMsg.Eventkey == 'mpGuide':
                        content = u"编写中，尚未完成".encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            print "暂且不处理"
            return reply.Msg().send()
        except Exception, Argment:
            return Argment
