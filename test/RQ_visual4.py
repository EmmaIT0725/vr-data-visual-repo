import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)

# Bar Plot Visualization

# 선택하여 열 이름 변경하기
df.rename(columns={'Social skills training for Autistic individuals':'Special Education'}, inplace=True)
df.rename(columns={'occupational safety and health':'Safety'}, inplace=True)
df.rename(columns={'Teacher training in Higher Education':'Teacher Education'}, inplace=True)

df['Educational Level'].loc[28] = 'K-12'
print(df['Educational Level'].value_counts())

import matplotlib.pyplot as plt

# fig, ax = plt.subplots()
fig, ax = plt.subplots(1,1)
fig.set_size_inches(10, 7.5)
educational_level = ['Higher Ed', 'K-12', 'Not specified']
counts = [23, 6, 1]
bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

#ax.barh(fruits, counts, label=bar_labels, color=bar_colors)
# legend 있는 code
# bar = ax.bar(educational_level, counts, label=bar_labels, color=bar_colors)

bar = ax.bar(educational_level, counts, color=bar_colors, width=0.9)

# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % height, ha='center', va='bottom', size = 13.5)
    # %.1f: 소수점 한 자리까지

# ax.set_ylabel('Count')
# ax.set_title('The number of Educational Level', fontsize=20)
# ax.legend(title='Educational Level')

plt.show()

df2 = df['Mission (Quest/Task)']
df2.value_counts()

fig, ax = plt.subplots(1,1)
fig.set_size_inches(13, 7)
# fig, ax로 받아서 작업할 때 위와 같이 크기 조절

mission = ['Goodwill Quests', 'Collection Quests', 'Recipe Quests', 'Escort Quests', 'Detective Quests', 'Messenger Quests']
counts = [12, 7, 6, 3, 1, 1]
# bar_labels = ['Goodwill Quests', 'Collection Quests', 'Recipe Quests', 'Escort Quests', 'Detective Quests', 'Messenger Quests']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange', 'tab:olive', 'tab:pink', 'tab:purple']

bar = ax.bar(mission, counts, color=bar_colors, width = 0.9)

# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % height, ha='center', va='bottom', size = 13.5)

# ax.set_ylabel('Count')
# ax.set_title('The number of Mission (Quest/Task)', fontsize=20)
# ax.legend(title='Mission (Quest/Task)')

plt.show()

df3 = df['Cover Story (Context)']
df3.value_counts()

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(9, 6)
# fig, ax로 받아서 작업할 때 위와 같이 크기 조절

coverstory = ['None', '1 included', '2 included', '3 included']
counts = [2, 2, 12, 14]
# bar_labels = ['0', '1', '2', '3']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange', 'tab:olive']

#ax.barh(fruits, counts, label=bar_labels, color=bar_colors)

# legend 있는 코드
# bar = ax.bar(coverstory, counts, label=bar_labels, color=bar_colors)

bar = ax.bar(coverstory, counts, color=bar_colors, width=0.9)

# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % height, ha='center', va='bottom', size=13.5)

# ax.set_ylabel('Count')
# ax.set_title('[Unit: features]\n', fontsize=15)
# ax.legend(title='Cover Story [Unit: features]')

plt.show()

df4 = df['Resources']
df4.value_counts()

import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(6, 6)
# fig, ax로 받아서 작업할 때 위와 같이 크기 조절

resources = ['Embedded in VR', 'Offered outside of VR', 'Not specified']
counts = [15, 9, 6]
# bar_labels = ['Embedded in VR', 'Offered outside of VR', 'N/A']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

bar = ax.bar(resources, counts, color=bar_colors, width = 0.9)

# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % height, ha='center', va='bottom', size=13)

# ax.set_ylabel('Count')
# ax.set_title('The number of Resource', fontsize=20)
# ax.legend(title='Resource')
plt.show()

df5 = df['Feedback']
print(df5.value_counts())

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(6, 6)
# fig, ax로 받아서 작업할 때 위와 같이 크기 조절
# https://github.com/Park-Young-Bin/Python_Projects/blob/master/%EA%B7%B8%EB%9E%98%ED%94%84%20%EC%84%9C%EC%8B%9D%20%EC%84%A4%EC%A0%95(matplotlib,%20seaborn).ipynb

feedback = ['Verification', 'Elaboration', 'Not specified']
counts = [13, 8, 9]
# bar_labels = ['Verification', 'Elaboration', 'N/A']
bar_colors = ['tab:red', 'tab:blue', 'tab:olive']

bar = ax.bar(feedback, counts, color=bar_colors, width = 0.9)

# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % height, ha='center', va='bottom', size=13)

# ax.set_ylabel('Count')
# ax.set_title('The number of Feedback', fontsize=20)
# ax.legend(title='Feedback')

plt.show()

df6 = df['Subject']
df6.value_counts()

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(13, 6)

subject = ['Safety','Nursing','Medicine','Business','Language','Teacher Education','Engineering','Ecology','Special Education','Biology', 'Science', 'Relationship and Sex\n Education(RSE)']
counts = [6,6,6,3,2,1,1,1,1,1,1,1]
# bar_labels = ['Occupational Safety and Health','Nursing','Medicine','Business','Language','Teacher training in Higher Education','Engineering','Ecology','Social skills training for Autistic Individuals','Biology']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange','tab:olive', 'tab:cyan', 'tab:pink', 'tab:purple', 'tab:green', 'tab:brown', 'tab:gray']

bar = ax.barh(subject, counts, color=bar_colors, height = 0.9)


# 가로 막대그래프 위에 값 표시하기
for idx, value in enumerate(counts):
    plt.text(value+0.05, idx, str(value))

# ax.set_ylabel('Count')
# ax.set_title('The number of Subject', fontsize=20)
# ax.legend(title='Subject')

plt.show()

df7 = df['Knowledge Domain']
df7.value_counts()

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(11, 6)

knowledge = ['Cognitive, Psychomotor', 'Cognitive', 'Cognitive, Affective', 'Cognitive, Affective, Psychomotor']
counts = [13, 9, 7, 1]
# bar_labels = ['Cognitive Psychomotor', 'Cognitive', 'Cognitive Affective', 'Cognitive Affective Psychomotor']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange', 'tab:olive']

bar = ax.bar(knowledge, counts, color=bar_colors, width = 0.9)

# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % height, ha='center', va='bottom', size=13.5)

# ax.set_ylabel('Count')
# ax.set_title('The number of Knowledge Domain', fontsize=20)
# ax.legend(title='Knowledge Domain')