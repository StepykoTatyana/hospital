import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

general = pd.read_csv('general.csv')
prenatal = pd.read_csv('prenatal.csv')
sports = pd.read_csv('sports.csv')
general.columns = ['Unnamed', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi', 'diagnosis', 'blood_test', 'ecg',
                   'ultrasound', 'mri', 'xray', 'children', 'months']
prenatal.columns = ['Unnamed', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi', 'diagnosis', 'blood_test', 'ecg',
                    'ultrasound', 'mri', 'xray', 'children', 'months']
sports.columns = ['Unnamed', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi', 'diagnosis', 'blood_test', 'ecg',
                  'ultrasound', 'mri', 'xray', 'children', 'months']

prenatal['gender'].replace(np.NaN, 'f', inplace=True)
sports['gender'].replace('female', 'f', inplace=True)
sports['gender'].replace('male', 'm', inplace=True)
general['gender'].replace('man', 'm', inplace=True)
general['gender'].replace('woman', 'f', inplace=True)

common_table = pd.concat([general, prenatal, sports], ignore_index=True)
common_table.drop(columns='Unnamed', inplace=True)
common_table['xray'].replace(np.NaN, 0, inplace=True)
common_table['bmi'].replace(np.NaN, 0, inplace=True)
common_table['mri'].replace(np.NaN, 0, inplace=True)
common_table['ecg'].replace(np.NaN, 0, inplace=True)
common_table['diagnosis'].replace(np.NaN, 0, inplace=True)
common_table['blood_test'].replace(np.NaN, 0, inplace=True)
common_table['ultrasound'].replace(np.NaN, 0, inplace=True)
common_table['children'].replace(np.NaN, 0, inplace=True)
common_table['months'].replace(np.NaN, 0, inplace=True)
common_table.replace('', np.NaN)
common_table.dropna(how='all')

# Decide 1st question:
maximum_name = common_table['hospital'].mode()[0]
print('The answer to the 1st question is', maximum_name)
'''common_table['hospital'].value_counts(dropna=True).plot.bar()
plt.show()'''
# Decide 2nd question:
common_diagnosis = common_table['diagnosis'].mode()[0]
print('The answer to the 2nd question is', common_diagnosis)
common_table['diagnosis'].value_counts(dropna=True).plot(kind='pie', subplots=True)
plt.show()
print("The answer to the 3rd question: It's because ")

'''
print(common_table['hospital'].shape[0])
print(common_table.loc[common_table.hospital == 'general'].shape[0])
print(common_table.loc[common_table.hospital == 'sports'].shape[0])
print(common_table.loc[common_table.hospital == 'prenatal'].shape[0])

index_d = [a for a in range(1, common_table.shape[0] + 1)]

common_table.set_index([index_d], inplace=True)
fig, axes = plt.subplots()

sns.violinplot('hospital', [common_table.loc[common_table.hospital == 'general'].shape[0],
                            common_table.loc[common_table.hospital == 'sports'].shape[0],
                            common_table.loc[common_table.hospital == 'prenatal'].shape[0]],
               data=common_table, ax=axes)
axes.yaxis.grid(True)
plt.show()'''
