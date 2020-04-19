from selenium import webdriver

driver= webdriver.Chrome('C:\\chromedriver.exe')
url= 'https://www.melon.com/chart/index.htm'
driver.get(url)

songs= driver.find_element_by_css_selector('#lst50')
print(type(songs))

# 1위부터 50위까지 data 뽑아내기
for song in songs:
    title= song.find_element_by_css_selector('span> a')
    print(title[0].text, title[1].text, sep= "-")