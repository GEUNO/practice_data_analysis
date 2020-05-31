# data filtering

import pandas as pd

sample_1= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx'
                        , header= 1
                        , skipfooter= 2
                        , usecols= 'A:C')
sample_1['기준년월']= '2020-05'
print(sample_1.head(0))

condi= sample_1['성별']=='남성'     # 특정 칼럼에 필터링 조건 설정(조건 연산자 ==, !=, >=, <=)
# print(condi)        # 일치하는 경우 True 불일치하는 경우 False 출력하는 class
print(type(condi))
print(sample_1[condi])      # 조건과 일치하는 행만 출력

condi_mul= (sample_1['성별'] != '남성') & (sample_1['입국객수'] >= 150000)        # 복수 조건의 경우 논리 연산자 &, | 이용
print('>>>>> 복수 조건의 경우 연산자 이용', sample_1[condi_mul], sep= '\n')

condi_mul_2= sample_1['국적코드'].isin(['A01', 'A18'])      # 한 칼럼에 대한 복수조건은 isin 함수사용
print(sample_1[condi_mul_2])
print(sample_1[condi_mul_2==False])     # 반대조건으로 필터링 시 조건을 False 로 설정
