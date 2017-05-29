# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
from tmp import novel
import email_sample
import movice
import sudoku
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
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    if recMsg.Content.split('.')[0]=='king':
                        page=recMsg.Content.split('.')[1]
                        head=recMsg.Content.split('.')[0]
                        content,txt= novel.Choose(head,page)
                        email_sample.email(page,txt)
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    elif recMsg.Content.split(':')[0]=='sudoku':
                        a=recMsg.Content.split(':')[1]
                        sudoku.main(a)
                        content = sudoku.fin1
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                    else:
                        keywo=recMsg.Content
                        content=movice.Search_main(keywo)
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print "暂且不处理"
                return reply.Msg().send()
        except Exception, Argment:
            return Argment