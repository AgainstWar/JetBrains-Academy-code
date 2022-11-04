# write your code here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read the data
General = pd.read_csv(
    'C:/Users/Again/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/general.csv')
Prenatal = pd.read_csv(
    'C:/Users/Again/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/prenatal.csv')
Sports = pd.read_csv(
    'C:/Users/Again/PycharmProjects/Data Analysis for Hospitals/Data Analysis for Hospitals/task/test/sports.csv')
# modify the data
Prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
Sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
Merge_df = pd.concat([General, Prenatal, Sports], ignore_index=True)
Merge_df.drop(columns=['Unnamed: 0'], inplace=True)
Merge_df.dropna(axis=0, how='all', inplace=True)
Merge_df['gender'] = Merge_df['gender'].replace(['female', 'woman', 'male', 'man'], ['f', 'f', 'm', 'm'])
Merge_df['gender'].replace(np.nan, 'f', inplace=True)
Merge_df.fillna(0, inplace=True)
columns = ["bmi", "diagnosis", "blood_test", "ecg", "ultrasound", "mri", "xray", "children", "months"]
for col in columns:
    Merge_df[col] = Merge_df[col].fillna(0)

# answer the question

# Question 1
Age_df = Merge_df['age']
Age_hist = Age_df.plot(kind='hist', bins=[0, 15, 35, 55, 70, 80])
plt.show()
answer1 = '15-35'

# Question 2
Diagnostic_df = Merge_df['diagnosis']
Diagnosis_pie = Diagnostic_df.value_counts().plot(kind='pie', autopct='%.1f%%')
plt.show()
answer2 = 'pregnancy'

# Question 3
sns.violinplot(data=Merge_df, x='hospital', y='height', scale='count')
plt.show()
answer3 = "It's because the difference in unit of measurement ,there many people's height near the median and mean of height ,"

print(f'The answer to the 1st question: {answer1}')
print(f'The answer to the 2nd question: {answer2}')
print(f'The answer to the 3rd question: {answer3}')
