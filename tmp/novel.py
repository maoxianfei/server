#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
 *                             _ooOoo_
 *                            o8888888o
 *                            88" . "88
 *                            (| -_- |)
 *                            O\  =  /O
 *                         ____/`---'\____
 *                       .'  \\|     |//  `.
 *                      /  \\|||  :  |||//  \
 *                     /  _||||| -:- |||||-  \
 *                     |   | \\\  -  /// |   |
 *                     | \_|  ''\---/''  |   |
 *                     \  .-\__  `-`  ___/-. /
 *                   ___`. .'  /--.--\  `. . __
 *                ."" '<  `.___\_<|>_/___.'  >'"".
 *               | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *               \  \ `-.   \_ __\ /__ _/   .-` /  /
 *          ======`-.____`-.___\_____/___.-`____.-'======
 *                             `=---='
 *          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 *                     佛祖保佑        永无BUG
'''
import re
import os
import requests

def Query(url):
    '''
    查询小说目录
    :param url:小说目录链接
    :return:小说目录列表类型 [链接，章节名称]
    '''
    webdata=requests.get(url+'index.html')
    # webdata.encoding='gbk'
    pattern=re.compile('<dd><a href="(.*?)">(.*?)</a></dd>')
    # print webdata.text
    li=pattern.findall(webdata.text)
    li[:]=[list(c) for c in li]

    #为每个链接加上前缀
    for i in li:
        i[0]=url+i[0]
        # print str(i).decode('unicode-escape').encode('utf-8')
    print(u'-------------------\n共%d节内容' % len(li))
    print(u'最新章节:%s \n-------------------'%li[-1][1])
    return li

def Createfile(bookname='novel'):
    '''
    创建文件夹和文本文件
    :param bookname:
    :return:
    '''
    path ='./book/'+bookname+'.txt'
    if not os.path.exists('./book'):
        os.mkdir('./book')
        print("Create book floder success")
    if not os.path.exists(path):
        with open(path, 'w') as d:
            d.write('test begin\n')
    return path
def Download(url_chapter):
    '''
    下载章节内容
    :param url_chapter: 每一章节的url
    :return:
    '''
    page=requests.get(url_chapter)
    # page.encoding='gbk'
    # print(u'状态码：'),page.status_code
    pattenr=re.compile('<!--go-->(.*)<!--over-->',re.S)#换行匹配
    page_text=pattenr.findall(page.text)
    Chinese="[^\u4e00-\u9fa5，]"#替换除了中文字符和逗号的所有字符
    page_text1=re.sub(Chinese,'',str(page_text))

    a=page_text1.decode('unicode-escape').encode('utf-8')
    final=re.sub("nbsp\;nbsp\;",' ',str(a))
    final1 = re.sub("<br><br>", ' ',final)
    content=str(final1)[2:-1]
    return content
def Choose(head='king',chap='1060'):
    page=int(chap)
    url={'Poor Rise':'http://www.aiquxs.com/read/46/46745/',
        'king':'http://www.aiquxs.com/read/67/67831/',
    'Poor Champion':'http://www.aiquxs.com/read/46/46800/',}
    li=Query(url[head])
    index=[]
    desc=[]
    i=0
    while li[page][1]!=li[-1][1]:
        index.append(page)
        desc.append(li[page][1])
        page=page+1
        i=i+1

    txt=Download(li[page][0])
    catalog=[]
    for i in range(len(index)):
        catalog.append(str(index[i])+desc[i])
    catalog=str(catalog).decode('unicode-escape').encode('utf-8')
    catalog=re.sub(",", '\n', catalog)#逗号换成换行符
    other = "[u\'\[\]]"  # 替换除了中文字符和逗号的所有字符
    catalog = re.sub(other, '', catalog)

    return catalog,txt

def Duplicate(tmp):
    patterns = []
    for line in tmp.split("\n"):
        if line not in patterns:
            # print('line=',line)
            patterns.append(line)
    print(u"去重后的列表:\n>>>"),patterns
    sum=''
    for patt in patterns:
        sum=sum+patt+'\n'
    # print('sum='+sum)
    return sum
def getconfig(head):
    '''
    :param head: 读取小说存储记录
    :return: 返回记录（str）
    '''
    if not os.path.exists('./update.ini'):
        open('./update.ini', 'w+')
    with open('./update.ini','r') as r:
        tmp=r.read()
        a=re.findall(head+'=(.*?)',tmp)
    # print(u'>>>读取小说:'),head,'=',a[0]
    if a[0]!='':
        return a[0]
    else:
        return -1
def writeconfig(head,page):
    '''
    :param head: 写入小说名字
    :param page: 写入最新章节，如果重复则覆盖，没有则添加到末尾
    :return:
    '''
    page=str(page)
    if not os.path.exists('./update.ini'):
        open('./update.ini', 'w+')
    with open('./update.ini','r+') as f:
        tmp=f.read()
        tmp1=re.sub(head+'='+'\d+',head+'='+page,tmp)
        if tmp1==tmp:
            print(u'已经为最新或内容没添加')
            with open('./update.ini', 'a+') as f:
                f.write(head + '=' + page)
            with open('./update.ini', 'r') as f:
                dup=f.read()
            with open('./update.ini', 'w') as f:
                dup2=Duplicate(dup)
                print(u'去重后记录文件：\n'),dup2
                f.write(dup2)
        else:
            print(u'有记录,修改原记录')
            with open('./update.ini', 'w+') as f:
                f.write(tmp1)
                print (tmp1)
    print(u'>>>数据写入完成')

