from bs4 import BeautifulSoup

html= '''
<html>
    <head>
    </head>
    <body>
        <h1> 우리동네시장</h1>
            <div class= 'sale'>
                <p id='fruits1' class='fruits'>
                    <span class= 'name'> 바나나 </span>
                    <span class= 'price'> 3000원 </span>
                    <span class= 'inventory'> 500개 </span>
                    <span class= 'store'> 가나다상회 </span>
                    <a href= 'http://bit.ly/forPlaywithData'> 홈페이지 </a>
                </p>
            </div>
            <div class= 'prepare'>
                <p id= 'fruits2' class= 'fruits'>
                    <span class= 'name'> 파인애플 </span>
                </p>
            </div>
    </body>
</html>
'''

soup= BeautifulSoup(html, 'html.parser')
print(soup)

tags_span= soup.select('span')
tags_p= soup.select('p')
ids_fruits1= soup.select('#fruits1')
class_price= soup.select('.price')
tags_span_class_price= soup.select('span.price')

# print(tags_span)
# print(tags_span_class_price)

tags_name= soup.select('span.name')
print(tags_name)

# 같은 태그를 찾더라도 여러가지 방식이 있다. (상위구조 등)
# 결과는 list 형태로 반환
tags_banana1= soup.select('#fruits1> span.name')
tags_banana2= soup.select('div.sale> #fruits1> span.name')
tags_banana3= soup.select('div.sale span.name')
print(tags_banana1)
print(tags_banana2)
print(tags_banana3)

# HTML에서 원하는 정보 가져오기
tags= soup.select('a')         # a 태그 내용 가져오기
print(tags, type(tags))
tag= tags[0]         # a 태그 내용 중 가장 첫 번째 항목 tag 변수 저장
print(tag, type(tag))
content= tag.text            # tag의 내용 중 txt 를 content 변수 저장
print(content, type(content))
link= tag['href']           # tag의 내용 중 URL 부분 link 변수 저장
print(link, type(link))