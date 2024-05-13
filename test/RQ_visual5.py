import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)

df_pivot1 = df.pivot_table(columns=['Knowledge Domain'], index=['Subject'], values='Subject_Num', aggfunc='count')
print(df_pivot1)

df_pivot1.sort_values(by='Cognitive', ascending=False).plot(kind='barh', stacked=True, rot=0, figsize=(12, 6), grid=False, legend='reverse', width = 0.75)

df_pivot2 = df.pivot_table(columns=['Cover Story (Context)'], index=['Mission (Quest/Task)'], values='Mission_Num', aggfunc='count')
df_pivot2

df_pivot2.sort_values(by='1개', ascending=False).plot(kind='bar', stacked=True, rot=0, figsize=(12, 7),
                                                            grid=False, legend='reverse', width = 0.8)
plt.legend(['None', '1 included', '2 included', '3 included'])

plt.show()

df.fillna('0', inplace=True)

df_pivot3 = df.pivot_table(columns=['Feedback'], index=['Operation (Activities)'], values='Operation_Num',
                           aggfunc='count')
df_pivot3

df_pivot3.sort_values(by='Elaboration', ascending=False).plot(kind='bar', stacked=True, rot=0, figsize=(8, 6),
                                                     grid=True, legend='reverse')

plt.legend(['Verification', 'Elaboration', 'Not specified'])
# x 축의 눈금 설정
plt.yticks([0, 3, 6, 9, 12, 15, 18])  # 원하는 눈금 값으로 설정
plt.show()