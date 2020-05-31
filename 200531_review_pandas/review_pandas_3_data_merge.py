# data merge

import pandas as pd

sample_1= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx'
                        , header= 1
                        , skipfooter= 2
                        , usecols= 'A:C')
sample_1['기준년월']= '2020-05'
print(sample_1.head(0))

code_master= pd.read_excel('C:\\examples_py\\files_200412\\sample_codemaster.xlsx')
print(code_master.head(0))

sample_1_merged= pd.merge(left= sample_1
                          , right= code_master
                          , how= 'left'                 # inner 지정시 일치하는 항목만 merge
                          , left_on= '국적코드'
                          , right_on= '국적코드')

print((sample_1_merged))

sample_1_merged.to_excel('C:\\examples_py\\files_200412\\sample_1_merged.xlsx')





# sample_2_merge 생성

sample_1_merged=pd.read_excel('C:\\examples_py\\files_200412\\sample_1_merged.xlsx'
                              , usecols= 'B:F')
print(sample_1_merged.head(0))
# print((sample_1_merged))

sample_2= pd.read_excel('C:\\examples_py\\files_200412\\sample_2.xlsx'
                        , header= 1
                        , skipfooter= 2
                        , usecols= "A:C")
# print(sample_2)
sample_2['기준년월']= '2020-06'

code_master= pd.read_excel('C:\\examples_py\\files_200412\\sample_codemaster.xlsx')
# print(code_master)

sample_2_merged= pd.merge(left= sample_2, right= code_master
                          , how= 'left'
                          , left_on= '국적코드', right_on= '국적코드')
print(sample_2_merged)
print(sample_1_merged)

sample_2_merged.to_excel('C:\\examples_py\\files_200412\\sample_2_merged.xlsx')