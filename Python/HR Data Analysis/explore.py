import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
            'B_office_data.xml' not in os.listdir('../Data') and
            'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here
    # read the data
    A_Office = pd.read_xml('../Data/A_office_data.xml')
    B_Office = pd.read_xml('../Data/B_office_data.xml')
    Hr_Data = pd.read_xml('../Data/hr_data.xml')

    # reindex the data

    for i in A_Office['employee_office_id']:
        A_Office['employee_office_id'].replace(i, 'A' + str(i), inplace=True)
    for i in B_Office['employee_office_id']:
        B_Office['employee_office_id'].replace(i, 'B' + str(i), inplace=True)

    B_Office.set_index('employee_office_id', inplace=True)
    A_Office.set_index('employee_office_id', inplace=True)
    Hr_Data.set_index('employee_id', inplace=True)

    # merge the data
    A_B_Data = pd.concat([A_Office, B_Office])
    # print(A_B_Data.columns)
    final_df = A_B_Data.merge(Hr_Data, left_index=True, right_index=True, indicator=True)
    # print(final_df.columns)
    final_df.drop(columns=['_merge'], inplace=True)
    # print(final_df.columns)
    final_df.sort_index(inplace=True)
    # print(final_df.index.tolist())
    # print(final_df.columns.tolist())

    # extract the data
    data_piovt_1 = final_df.pivot_table(index='Department',
                                        columns=['left', 'salary'],
                                        values='average_monthly_hours',
                                        aggfunc='median').round(2)
    data_piovt_1 = data_piovt_1.loc[
        (data_piovt_1[1, 'high'] > data_piovt_1[1, 'low']) & (data_piovt_1[0, 'high'] < data_piovt_1[0, 'medium'])]

    data_piovt_2 = final_df.pivot_table(index='time_spend_company',
                                        columns='promotion_last_5years',
                                        values=['satisfaction_level', 'last_evaluation'],
                                        aggfunc=['min', 'max', 'mean']).round(2)
    data_piovt_2 = data_piovt_2.loc[
        (data_piovt_2['mean', 'last_evaluation'][0]) > (data_piovt_2['mean', 'last_evaluation'][1])]

    # print the data
    print(data_piovt_1.to_dict())
    print(data_piovt_2.to_dict())
