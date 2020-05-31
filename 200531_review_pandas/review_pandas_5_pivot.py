# using pivot table func

import pandas as pd
sample= pd.read_excel('C:\\examples_py\\files_200412\\sample_merged_200531.xlsx')
# print(sample)

sample_pivot= sample.pivot_table(values='입국객수'
                                 , index= '기준년월'
                                 , columns= '국적명'
                                 , aggfunc= 'sum')                  # mean/ sum/ min/ max/ median/ count
print(sample_pivot)