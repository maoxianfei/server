# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
from tmp import novel
a=u'''
第一千零五十八章 战术为王
天才壹秒記住『愛♂去7小?說→網WAiQuSCom』，為您提供精彩小說閱讀。   在他之前的战例之中，其中有一次甚至是让这制式机甲在他的重新组装和功能完成时，达到了黑级机甲的攻防能力。   这可是机甲战，魂师是不能离开机甲的，只能用武魂辅助机甲战斗。制式机甲怎么和黑级机甲比拼？   几乎所有人在和他战斗的时候都会选择全力爆发，不给他重塑机甲的机会，可直到现在，还没有人成功过。   唐舞麟的长枪落地，终究还是没能命中对手。而那位金属大师凭借着迅速完成的推进器，推动着他的制式机甲以更快的速度向远处绕去。他现在需要做的，就是掌控好距离，完成机甲改造，再回身干掉唐舞麟就是了。   在他推进器完成的时候，是双方距离最近的时候，大约相隔一百五十米左右。   唐舞麟飞快的追向他，可他的速度实在是太快了，根本就不可能追的上。这是机甲本质上的差距。   唐舞麟的武魂再强，也不可能让自己的机甲推进器超负荷加速。这是机甲本身品质所决定的。   就在所有人都认为，这场比赛要朝着两位解说所说的方向发展的时候。唐舞麟突然就爆发了。
'''


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
                        # a= novel.Choose(head,page)
                        # content=a.decode('unicode-escape').encode('utf-8')
                        content=a
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
