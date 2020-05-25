import os
import requests
from lxml import etree

def login(userid, userpw, ISPsel):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
	base_url = 'https://i.njtech.edu.cn/redirectsso.php'
	s = requests.Session()
	r = s.get(base_url,headers=headers)
	root = etree.HTML(r.content)
	lt = root.xpath('//input[@name="lt"]/@value')[0]
	execution = root.xpath('//input[@name="execution"]/@value')[0]
	service = r.url.split('service=')[-1]
	SetCookie = r.headers['Set-Cookie']
	JSESSION = SetCookie.split('=')[1].split(';')[0]
	ISP = {'中国移动':'cmcc','中国电信':'telecom'}
	channelshow = ISPsel
	provider = ISP[channelshow]
	posturl = 'https://u.njtech.edu.cn/cas/login;'+'jsessionid='+JSESSION+'?service='+service
	formdata = {'username':userid,'password':userpw,'channelshow': channelshow,'channel': '@'+provider,'lt':lt,'execution':execution,'_eventId':'submit','login':'登录'}
	insertcookie = s.cookies.get_dict()['insert_cookie']
	postheaders = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','Referer':r.url,'Cookie':'JSESSIONID='+JSESSION+'; insert_cookie='+insertcookie}
	postr = s.post(posturl,data=formdata,headers=postheaders)
	postr.encoding = postr.apparent_encoding
	successstr = '您已经登录成功'
	if successstr in postr.text:
		print('已登录')
	else:
		print('出现异常')

def main():
	userid = '14031701xx'	#10位学号,字符串类型
	userpw = 'xxxxxxxxxx'	#密码，字符串类型
	ISPsel = '中国移动'		#运营商名称(中国移动/中国电信)，字符串类型
	login(userid,userpw,ISPsel)
	os.system('pause')

if __name__ == '__main__':
	main()
