from bs4 import BeautifulSoup
import requests
check=requests.get('https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/').text
ano=BeautifulSoup(check,'lxml')
title=ano.find('title')
webtext=ano.find('div',class_='td-post-content tagdiv-type')
para=webtext.find('p')
#inorder to get the link info job.para.h.a['href']
print(f'''
      {title.text}
      {webtext.text.strip()}
      ''')
# header=ano.find('html',class_='text')
# h1s=header.find_all('p')
# for k in :
#     print(k.text)
# print(title.text)
# print(check)