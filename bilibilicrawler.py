import requests
from lxml import etree

maxav=input("请输入最大av号：")
maxav=int(maxav)
link='https://www.bilibili.com/video/av'
headers={
    'user-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50'
}

for avnum in range(7,maxav+1):
    link2=link+str(avnum)+'/'
    page=requests.get(link2,headers=headers)
    html=etree.HTML(page.text)
    title=html.xpath('//*[@id="viewbox_report"]/div[1]/div[1]/h1/text()')
    if len(title)==1:
        print('av'+str(avnum)+title[0])
