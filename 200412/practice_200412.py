import pandas as pd

sample_1= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx',
                        header= 1,
                        skipfooter= 2,      #마지막 2행은 제외
                        usecols= 'A:C')         #가져올 칼럼
# print(sample_1.info())
# print(sample_1.head(2))
# print(sample_1.tail(2))
# 기초 통계량
# print(sample_1.describe())

# print(sample_1)
# print(type(sample_1))

# 필요한 칼럼은 list 형태로 지정할 수 있다
# print(sample_1[['국적코드', '입국객수']])

# 새로운 칼럼 형성 및 data 추가
sample_1['기준년월']='2020-04'
print(sample_1)

# 조건연산자를 사용해서 필요한 low 정보 필터링
condi_1= (sample_1['국적코드']=='A01')
# print(sample_1[condi_1])
# print(sample_1[condi_1==False])

# isin 함수를 사용하여 복수의 low 정보 필터링
condi_2= (sample_1['성별'].isin(['남성', '여성']))
# print(sample_1[condi_2])
# print(sample_1[condi_2==False])

