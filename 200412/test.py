import pandas as pd

sample_1= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx',
                        header= 1,
                        skipfooter= 2,      #마지막 2행은 제외
                        usecols= 'A:ZZ')         #가져올 칼럼, 빈칸은 가져오지 않음

print(len(sample_1))

sample_1['cols_add']= 'end'

print(sample_1)

sample_1.to_excel('C:\\examples_py\\files_200412\\test_length.xlsx', index= False)