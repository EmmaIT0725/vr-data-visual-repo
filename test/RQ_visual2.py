import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)

print(df['Subject(2D)'].value_counts())
print(df['Feedback'].value_counts())
df['Feedback'].loc[24]='Not specified'
print(df['Feedback'].loc[24])
print(df['Feedback'].loc[25])
df.replace('nan', 'Not specified', regex=True, inplace=True)
df.replace('NaN', 'Not specified', regex=True, inplace=True)

# Create fig and grid spec
fig = plt.figure(figsize=(10, 10), dpi=80)
grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)

# 축을 정의하기
# 틱 (Tick)은 그래프의 축에 간격을 구분하기 위해 표시하는 눈금입니다.
ax = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])


# 메인 그래프에 Subject 산점도 그리기
# fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(df['Subject(2D)'], df['Subject'],
                linewidths=0.5, edgecolors='k', alpha=1,
                s=((df['Subject_Value_Counts']) + 5) ** 2.5, c=df['Subject_Value_Counts'], cmap='hsv')
# scatter 함수의 매개 변수 s : 도형의 크기 지정
# scatter 함수의 매개 변수 c : 색상 이름 또는 숫자의 연속형
ax.set_title('Correlation between Subject and Subject(2D)')
ax.set_ylabel('Subject')
# y축 회전하기
# plt.yticks(rotation=0) ## y label 회전하지 않기
# x축 회전하기
plt.xticks(rotation=75) ## x label 회전하기 --> figsize 늘리기
# 산점도 색 막대
# fig.colorbar(sc)
fig.show()

# 하단에 histogram
ax_bottom.hist(df['Subject(2D)'], 40, histtype='barstacked', orientation='vertical', color='lightpink', edgecolor = 'k' ,linewidth = 1.0, rwidth = 5.0)

# x = df['Subject(2D)_Num']
# y = df['Subjecct(2D)'].value_counts()
# for i, v in enumerate(x):
#     plt.text(v, y[i], y[i],                 
#              # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
#              fontsize = 12, 
#              color='blue',
#              horizontalalignment='center',  # horizontalalignment (left, center, right)
#              verticalalignment='top')    # verticalalignment (top, center, bottom)

# histtype='stepfilled' / 'barstacked', 'step'
# edgecolor : 선으로 구분
# linewidth : 선 굵기 설정
# ax_bottom.xlabel('Subject(2D)')
# ax_bottom.ylabel('Subject')
ax_bottom.invert_yaxis()

# 오른쪽에 histogram
ax_right.hist(df['Subject'], 40, histtype='barstacked', orientation='horizontal', color='lightblue', edgecolor = 'k' ,linewidth = 1.0, rwidth = 2.0)
# Decorations
ax.set(title='Subject, Subject(2D) and Knowledge Domain', xlabel='Subject(2D)', ylabel='Subject')
ax.title.set_fontsize(20)
for item in ([ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(14)