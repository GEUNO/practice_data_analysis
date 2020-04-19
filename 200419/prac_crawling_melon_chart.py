from selenium import webdriver

driver= webdriver.Chrome('C:\\chromedriver.exe')

url= 'https://www.melon.com/chart/index.htm'
driver.get(url)

from bs4 import BeautifulSoup

html= driver.page_source
soup= BeautifulSoup(html, 'html.parser')

# print(soup)

songs= soup.select('#lst50')
# print(len(songs))
# print(songs[0])

# song= songs[0]
# title= song.select('a')
# print(len(title))
# print(title)

# title_2= song.select('span> a')
# print((len(title_2)))
# print(title_2)
# print(title_2[0].text, '-', title_2[1].text)

print(("*"*50))
# 1위부터 50위까지 data 뽑아내기
for song in songs:
    title= song.select('span> a')
    print(title[0].text, title[1].text, sep= "-")
