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
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    if recMsg.Content.split('.')=='a':
                        content = "test"
                    else:
                        content='''中蜂拥而出。这些蓝银皇向四周伸展，化为一根根如同触手一般的存在，每一根的长度都超过了五十米，两侧张开，横向宽度足以控制百米。   星斗战网全联邦挑战赛的场地虽然大，但那也是有限的。当唐舞麟那一根根仿佛有着金色骨骼一般的蓝银皇张开之后，控制的范围就大大的增加了。虽然他的速度不如对手，但凭借着控制范围，还是有可能压缩对方生存空间的。   果不其然，正在改造机甲的金属大师就没有那么轻松了。他只能再改造了一个推进器，帮助自己更灵活的改变方向，全场飞奔。同时，开始改造机甲主核心。   一旦主核心完成，提供给机甲的能量压缩程度就会不同，那时候，凭借着机甲的绝对优势，就足以压制唐舞麟了。   这位金属大师本身有着七环魂圣层次的修为，他的金属掌控和更高级别俄机甲相互结合，他有绝对信心获胜。   机甲在场地中纵横闪烁，速度奇快无比。唐舞麟虽然控制的范围大了，但却依旧怎么也追不上对手。   金属大师坐在驾驶舱内，全身都闪烁着金属的光泽，不断的改变着机甲，嘴角处已经流露出了胜利者的微笑。   机甲马上就能够达到紫级程度了，但自己一点都不用着急，什么时候改造到了黑级程度，再以雷霆万钧之势干掉对方，就像碾死一只内，全身都闪烁着金属的光泽，不断的改变着机甲，嘴角处已经流露出了胜利者的微笑。   机甲马上就能够达到紫级程度了，但自己一点都不用着急，什么时候改造到了黑级程度，再以雷霆万钧之势干掉对方，就像碾死一只内，全身都闪烁着金属的光泽，不断的改变着机甲，嘴角处已经流露出了胜利者的微笑。   机甲马上就能够达到紫级程度了，但自己一点都不用着急，什么时候改造到了黑级程度，再以雷霆万钧之势干掉对方，就像碾死一只'''
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