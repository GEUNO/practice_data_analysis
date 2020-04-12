import pandas as pd

sample_1= pd.read_excel('C:\\examples_py\\files_200412\\sample_1.xlsx',
                        header= 1,
                        skipfooter= 2,      #마지막 2행은 제외
                        usecols= 'A:C')         #가져올 칼럼

code_master= pd.read_excel('C:\\examples_py\\files_200412\\sample_codemaster.xlsx')

# print(sample_1)
# print(code_master)

sample_1_code= pd.merge(left= sample_1,
                        right= code_master,
                        how= 'left',            # inner 로 지정시 값이 일치하는 경우만 표기
                        left_on= '국적코드',
                        right_on= '국적코드')

print(sample_1_code)
