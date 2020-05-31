# column based data handling

import pandas as pd

sample_check= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx')
# print(sample_check)

sample_1= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx'
                        , header= 1
                        , skipfooter= 2
                        , usecols= 'A:C')
# print(sample_1)
# print(sample_1.head(3))
# print(sample_1.tail(3))

# print(sample_1.info())      # sample_1 의 기본 info 출력
# print(sample_1.describe())      # maple_1 의 기본 통계량 출력

print(sample_1.head(0))     # sample_1 의 칼럼명 출력
# print(sample_1['성별'])
# print(sample_1[['국적코드', '입국객수']])       # 특정 칼럼을 출력하려는 경우 list [] 사용가능

# sample_1_add_col= sample_1      # 새로운 DataFrame 형성
# sample_1_add_col['기준년월']= '2020-05'     # 새로운 칼럼 '기준년월' 생성
# print(sample_1_add_col['기준년월'])