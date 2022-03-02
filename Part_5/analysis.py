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

common_table = pd.concat([general, prenatal, sports], ignore_index=True)
common_table.drop(columns='Unnamed', inplace=True)
common_table = common_table.fillna(0)
for index, row in common_table.iterrows():
    if row['hospital'] == 0:
        common_table.drop(index=index, inplace=True)
common_table['gender'] = common_table['gender'].replace([0, 'female', 'woman'], 'f')
common_table['gender'] = common_table['gender'].replace(['male', 'man'], 'm')

# Decide 1st question:
# print(common_table['age'].loc[common_table['age'].between(15.0, 35.0)])
count_1 = common_table['age'].loc[common_table['age'].between(0.0, 15.0)].count()
count_2 = common_table['age'].loc[common_table['age'].between(15.0, 35.0)].count()
count_3 = common_table['age'].loc[common_table['age'].between(35.0, 55.0)].count()
count_4 = common_table['age'].loc[common_table['age'].between(55.0, 70.0)].count()
count_5 = common_table['age'].loc[common_table['age'].between(70.0, 80.0)].count()
maximum_people = 0
maximum_name = ''
for a in [count_1, count_2, count_3, count_4, count_5]:
    if a > maximum_people:
        maximum_people = a
if maximum_people == count_1:
    maximum_name = '0 - 15'
    common_table['age'].loc[common_table['age'].between(0.0, 15.0)].plot.hist(bins=50)
elif maximum_people == count_2:
    maximum_name = '15 - 35'
    common_table['age'].loc[common_table['age'].between(15.0, 35.0)].plot.hist(bins=50)
elif maximum_people == count_3:
    maximum_name = '35 - 55'
    common_table['age'].loc[common_table['age'].between(35.0, 55.0)].plot.hist(bins=50)
elif maximum_people == count_4:
    maximum_name = '55 - 70'
    common_table['age'].loc[common_table['age'].between(55.0, 70.0)].plot.hist(bins=50)
else:
    maximum_name = '70 - 80'
    common_table['age'].loc[common_table['age'].between(70.0, 80.0)].plot.hist(bins=50)
print('The answer to the 1st question:', maximum_name)
# print(common_table['age'].loc[common_table['age'].between(0.0, 15.0).between(15.0, 35.0)])
# print(count_1, count_2, count_3, count_4, count_5)
# common_table['age'].loc[common_table['age'].between(15.0, 35.0)].plot.hist(bins=50)
plt.show()
'''



# Decide 2nd question:
common_diagnosis = common_table.loc[common_table['hospital'] == 'sports'].reset_index()['diagnosis'].mode()[0]
common_table.loc[common_table['hospital'] == 'sports'].reset_index()['diagnosis'].value_counts(dropna=True).plot.pie()
plt.show()
print('The answer to the 2nd question is', common_diagnosis)
# Decide 3nd question:
print("The answer to the 3rd question: It's because in a general hospital accommodates people of different age, "
      "diagnosis, gender, unlike the sports and a prenatal hospitals where mainly young athletes and woman are "
      "registered")

index_general = [a for a in range(1, common_table.loc[common_table.hospital == 'general'].shape[0] + 1)]
index_sports = [a for a in range(1, common_table.loc[common_table.hospital == 'sports'].shape[0] + 1)]
index_prenatal = [a for a in range(1, common_table.loc[common_table.hospital == 'prenatal'].shape[0] + 1)]
index_new = index_general + index_prenatal + index_sports

common_table.set_index([index_new], inplace=True)
sns.set_theme(style="whitegrid")
ax = sns.violinplot(x=common_table["hospital"], y=common_table.index, palette="Set2", split=True,
                    scale="count")
plt.show()
'''


common_diagnosis = common_table.loc[common_table['hospital'] == 'sports'].reset_index()['diagnosis'].mode()[0]
print('The answer to the 2nd question:', common_diagnosis)
common_table.loc[common_table['hospital'] == 'sports'].reset_index()['diagnosis'].value_counts(dropna=True).plot.pie()
plt.show()