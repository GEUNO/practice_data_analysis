import pandas as pd

sample_1= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx',
                        header= 1,
                        skipfooter= 2,      #마지막 2행은 제외
                        usecols= 'A:C')         #가져올 칼럼

sample_1['기준년월']= '2020-03'

code_master= pd.read_excel('C:\\examples_py\\files_200412\\sample_codemaster.xlsx')

sample_1_code= pd.merge(left= sample_1,
                        right= code_master,
                        how= 'left',            # inner 로 지정시 값이 일치하는 경우만 표기
                        left_on= '국적코드',
                        right_on= '국적코드')


sample_2= pd.read_excel('C:\\examples_py\\files_200412\\sample_2.xlsx',
                        header= 1,
                        skipfooter= 2,
                        usecols= 'A:C')
sample_2['기준년월']= '2020-04'

code_master= pd.read_excel('C:\\examples_py\\files_200412\\sample_codemaster.xlsx')

sample_2_code= pd.merge(left= sample_2,
                        right= code_master,
                        how= 'left',
                        left_on= '국적코드',
                        right_on= '국적코드')

# vertical merge를 위해선 data의 형태가 동일해야 함
# print(sample_1_code)
# print(sample_2_code)

sample= sample_1_code.append(sample_2_code, ignore_index= True)         # True 지정시 순서대로 index 지정
print(sample)

sample.to_excel('C:\\examples_py\\files_200412\\result.xlsx', index= False)
sample.to_csv('C:\\examples_py\\files_200412\\result_csv.csv', index= False)

sample_pivot= sample.pivot_table(values= '입국객수',
                                 index= '국적명',
                                 columns= '기준년월',
                                 aggfunc= 'sum')            #값을 어느 기준으로 나타낼 것인가, min/max/avg/count 등

print(sample_pivot)

sample_pivot_2= sample.pivot_table(values= '입국객수',
                                   index= '국적명',
                                   aggfunc= 'sum')

print(sample_pivot_2)