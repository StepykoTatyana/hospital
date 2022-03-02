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
'''prenatal.replace('', np.nan, inplace=True)
prenatal.dropna()
sports.replace('', np.nan, inplace=True)
sports.dropna()
general.replace('', np.nan, inplace=True)
general.dropna()'''
prenatal['gender'].replace(np.NaN, 'f', inplace=True)
sports['gender'].replace('female', 'f', inplace=True)
sports['gender'].replace('male', 'm', inplace=True)
general['gender'].replace('man', 'm', inplace=True)
general['gender'].replace('woman', 'f', inplace=True)
common_table = pd.concat([general, prenatal, sports], ignore_index=True)
common_table.drop(columns='Unnamed', inplace=True)
# common_table.fillna(0, inplace=True)
# common_table.replace(0.0, 0, inplace=True)
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
print(common_table)
index_d = [a for a in range(1, common_table.shape[0] + 1)]

# common_table.set_index([index_d], inplace=True)
# print(common_table)
# common_table.to_csv('out.csv')

# Decide 1st question:
maximum_name = common_table['hospital'].mode()[0]
print('The answer to the 1st question is', maximum_name)
# common_table['hospital'].value_counts(dropna=True).plot.bar()

# Распространенное заболевания для спорт больницы
# print(common_table.loc[common_table['hospital'] == 'sports'].reset_index()['diagnosis'].mode()[0])
common_table.loc[common_table['hospital'] == 'sports'].reset_index()['diagnosis'].value_counts(dropna=True).plot.pie()
# plt.show()

# Распространенное заболевания для всех больницы
'''common_table['hospital'].value_counts(dropna=True).plot(kind='pie', subplots=True)
plt.show()'''
common_diagnosis = common_table['diagnosis'].mode()[0]
print('The answer to the 2nd question is', common_diagnosis)
common_table['hospital'].value_counts(dropna=True).plot(kind='pie', subplots=True)
plt.show()

index_new = []
# common_table['diagnosis'].value_counts(dropna=True).plot(kind='pie', subplots=True)
# sns.set_theme(style="whitegrid")
sns.violinplot(x=common_table['hospital'].value_counts(), data=common_table, split=True)
plt.show()
# print('The answer to the 3rd question is', round((count_dislocation / count_common_sports), 3))
