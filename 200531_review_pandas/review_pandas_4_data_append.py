# data append
import pandas as pd

sample_1_merged= pd.read_excel('C:\\examples_py\\files_200412\\sample_1_merged.xlsx', usecols="B:F")
sample_2_merged= pd.read_excel('C:\\examples_py\\files_200412\\sample_2_merged.xlsx', usecols="B:F")

# print(sample_1_merged, sample_2_merged, sep= '\n')

sample= sample_1_merged.append(sample_2_merged
                               , ignore_index= True)            # True 조건, index 새로 지정
print(sample)

condi=(sample['국적명']=='일본') & (sample['성별']=='여성')
print(sample[condi])

sample.to_excel('C:\\examples_py\\files_200412\\sample_merged_200531.xlsx'
                , index= False)         # Flase 조건, index 미저장

sample_read= pd.read_excel('C:\\examples_py\\files_200412\\sample_merged_200531.xlsx')
print(sample_read)