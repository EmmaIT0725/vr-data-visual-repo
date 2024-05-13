import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)

# Pie Chart
# https://wikidocs.net/137218

# Subject(2D) 파이차트 만들기 위해서 Applied/Pure, Soft/Hard 세분화하기
df_S2_list = df['Subject(2D)'].str.split(" ")
print(df_S2_list)
## 그 결과 리스트의 형태로 분리되어 저장됨
df['Subject(2D)_1'] = df_S2_list.str.get(0)
df['Subject(2D)_2'] = df_S2_list.str.get(1)

df.to_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')

new = df['Subject(2D)_1'].value_counts().sort_values()
plt.pie(new, startangle=135, explode=(0, 0.3), shadow=True, autopct='%1.1f%%')

# 차트 조각 색상 바꾸기 : colors
new = df['Subject(2D)_1'].value_counts().sort_values()
colors = ['cornflowerblue', 'darkorange' ]
plt.pie(new, startangle=135, explode=(0, 0.3), shadow=True, autopct='%1.1f%%', colors=colors)

# 텍스트 사이즈 변경 : textprops
new = df['Subject(2D)_1'].value_counts().sort_values()
colors = ['cornflowerblue', 'darkorange' ]
plt.pie(new, startangle=135, explode=(0, 0.3), shadow=True, autopct='%1.1f%%', colors=colors, textprops={'fontsize':15})
plt. show()


# Role 나타내기
new1 = df['Role'].value_counts().sort_values()
labels = ['Multiple', 'Single']
colors = ['mediumseagreen', 'crimson']
plt.pie(new1, labels=labels, startangle=135, explode=(0, 0.30), shadow=True, autopct='%1.1f%%', colors=colors, textprops={'fontsize':14})
# plt.title('[The ratio of Cover Story (Context)]\n', fontsize=15)
# plt.legend(labels=labels, loc='upper left', bbox_to_anchor=(0.999, 0.9))
plt.show()

# Applied 파이 차트
ratio = [62.96, 37.03]
labels = ['Soft', 'Hard']
colors = ['lightcoral', 'mediumaquamarine' ]
plt.pie(ratio, labels=labels, startangle=-130, explode=(0, 0.1), shadow=True, autopct='%1.1f%%', colors=colors, textprops={'fontsize':12})
plt.title('[The ratio of Subject(2D) _ Applied]', fontsize=14)

plt.legend(labels=labels, loc='upper left', bbox_to_anchor=(0.999, 0.8))
# plt.savefig("65세 이상.png",facecolor='#eeeeee', bbox_inches='tight')

# Pure 파이 차트
ratio = [100]
labels = ['Hard']
colors = ['lightcoral']
plt.pie(ratio, labels=labels, startangle=-130, shadow=True, autopct='%1.1f%%', colors=colors, textprops={'fontsize':12})
plt.title('[The ratio of Subject(2D) _ Pure]', fontsize=14)

plt.legend(labels=labels, loc='upper left', bbox_to_anchor=(0.999, 0.8))
# plt.savefig("65세 이상.png",facecolor='#eeeeee', bbox_inches='tight')

# Cover Story Pie Chart 나타내기
new = df['Cover Story (Context)'].value_counts().sort_values()
labels = ['None', '1 included', '2 included', '3 included']
colors = ['lightyellow', 'mediumseagreen', 'crimson', 'aqua']
plt.pie(new, labels=labels, startangle=90, explode=(0, 0, 0, 0.15), shadow=True, autopct='%1.1f%%', colors=colors, textprops={'fontsize':12})
plt.title('[The ratio of Cover Story (Context)]\n', fontsize=15)

plt.legend(labels=labels, loc='upper left', bbox_to_anchor=(0.999, 0.9))

new = df['Operation (Activities)'].value_counts().sort_values()
labels = ['Unguided', 'Guided']
colors = ['mediumseagreen', 'crimson']
plt.pie(new, labels=labels, startangle=90, explode=(0.1, 0), shadow=True, autopct='(%1.1f%%)', colors=colors, textprops={'fontsize':15})
# plt.title('The ratio of Operation (Activities)', fontsize=20)

# plt.legend(labels=labels, loc='upper left', bbox_to_anchor=(0.999, 0.9))
# plt.savefig("65세 이상.png",facecolor='#eeeeee', bbox_inches='tight')