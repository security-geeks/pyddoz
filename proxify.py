import requests
import re
import random

def make_request():
    urls = ['https://free-proxy-list.net/', 'https://www.sslproxies.org/', 'https://www.us-proxy.org/']
    headers = {
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	           'Accept-Encoding': 'none',
	           'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive',
	           'Content-Encoding': 'gzip',
	           'Content-Type': 'text/html; charset=utf-8'
               }
    response = requests.get(random.choice(urls), headers=headers).text
    return re.findall(r"<tr><td>[^<]*</td><td>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td>[^<]*</td><td class='hm'>[^<]*</td><td class='hx'>[^<]*</td><td class='hm'>[^<]*</td></tr>", response)

def one():
	match = random.choice(make_request())
	result = match.split('</td>')
	ip_address = result[0].strip('<tr><td>')
	port = result[1].strip('</td>')
	if result[6].strip('<td class=\'hx\'>') == 'ye':
		typ = 'https'
	else:
		typ = 'http'
	return typ + '://' + ip_address + ':' + port
