import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)


# 선택하여 열 이름 변경하기
df.rename(columns={'Social skills training for Autistic individuals':'Special Education'}, inplace=True)
df.rename(columns={'occupational safety and health':'Safety'}, inplace=True)
df.rename(columns={'Teacher training in Higher Education':'Teacher Education'}, inplace=True)

df['Educational Level'].loc[28] = 'K-12'
print(df['Educational Level'].value_counts())


# Bar Plot Visualization_Subject
import matplotlib.pyplot as plt

df6 = df['Subject']
df6.value_counts()

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(13, 6)

subject = ['Safety','Nursing','Medicine','Business','Language','Teacher Education','Engineering','Special Education', 'Science', 'Relationship and Sex\n Education(RSE)']
counts = [6,6,6,3,2,1,1,1,3,1]
# bar_labels = ['Occupational Safety and Health','Nursing','Medicine','Business','Language','Teacher training in Higher Education','Engineering','Ecology','Social skills training for Autistic Individuals','Biology']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange','tab:olive', 'tab:cyan', 'tab:purple', 'tab:green', 'tab:brown']

bar = ax.barh(subject, counts, color=bar_colors, height = 0.9)


# 가로 막대그래프 위에 값 표시하기
for idx, value in enumerate(counts):
    plt.text(value+0.05, idx, str(value))

# ax.set_ylabel('Count')
# ax.set_title('The number of Subject', fontsize=20)
# ax.legend(title='Subject')

plt.show()

# df7 = df['Knowledge Domain']
# df7.value_counts()

# fig, ax = plt.subplots(1, 1)
# fig.set_size_inches(11, 6)

# knowledge = ['Cognitive, Psychomotor', 'Cognitive', 'Cognitive, Affective', 'Cognitive, Affective, Psychomotor']
# counts = [13, 9, 7, 1]
# # bar_labels = ['Cognitive Psychomotor', 'Cognitive', 'Cognitive Affective', 'Cognitive Affective Psychomotor']
# bar_colors = ['tab:red', 'tab:blue', 'tab:orange', 'tab:olive']

# bar = ax.bar(knowledge, counts, color=bar_colors, width = 0.9)

# # 숫자 넣는 부분
# for rect in bar:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % height, ha='center', va='bottom', size=13.5)

# # ax.set_ylabel('Count')
# # ax.set_title('The number of Knowledge Domain', fontsize=20)
# # ax.legend(title='Knowledge Domain')

# Bar Plot Visualization_Subject & Knowledge Domain
df_pivot1 = df.pivot_table(columns=['Knowledge Domain'], index=['Subject'], values='Subject_Num', aggfunc='count')
print(df_pivot1)

# df_pivot1.sort_values(by='Cognitive', ascending=True).plot(kind='barh', stacked=True, rot=0, figsize=(12, 6), grid=False, legend='reverse', width = 0.75)
df_pivot1.sort_values(by='Cognitive', ascending=True).plot(kind='barh', stacked=True, rot=0, figsize=(12, 6), grid=False, width = 0.75)

# plt.legend(['Cognitive, Psychomotor', 'Cognitive', 'Cognitive, Affective', 'Cognitive, Affective, Psychomotor'])
plt.show()


# Bar Plot Visualization_Subject & Mission Quest
df_pivot2 = df.pivot_table(columns=['Mission (Quest/Task)'], index=['Subject'], values='Subject_Num', aggfunc='count')
print(df_pivot2)

# df_pivot2.sort_values(by='Goodwill Quests', ascending=False).plot(kind='barh', stacked=True, rot=0, figsize=(12, 6), grid=False, legend='reverse', width = 0.75)
df_pivot2.sort_values(by='Goodwill Quests', ascending=True).plot(kind='barh', stacked=True, rot=0, figsize=(12, 6), grid=False, width = 0.75)

# plt.legend(['Goodwill Quests', 'Recipe Quests', 'Detective Quests', 'Escort Quests', 'Collection Quests', 'Messenger Quests'])
plt.show()
