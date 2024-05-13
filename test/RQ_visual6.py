import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)

# Subject 산점도 그리기
fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(df['Subject(2D)'], df['Subject'],
                linewidths=0.5, edgecolors='k', alpha=1,
                s=(df['Subject_Value_Counts'] * 2) ** 2.5, c=df['Subject_Value_Counts'], cmap='hsv')
ax.set_title('Correlation between Subject and Subject(2D)')
fig.colorbar(sc)
fig.show()

# Mission마다 Role 산점도 그리기
fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(df['Role'], df['Mission (Quest/Task)'],
                linewidths=0.5, edgecolors='k', alpha=1,
                s=(df['Mission_Value_Counts'] + 2) ** 2.5, c=df['Mission_Value_Counts'], cmap='hsv')
ax.set_title('Correlation between Role and Mission (Quest/Task)')
fig.colorbar(sc)
fig.show()

# Knowledge Domain & Educational Level

df_pivot1_1 = df.pivot_table(columns=['Educational Level'], index=['Knowledge Domain'], values='Knowledge Domain_Num', aggfunc='count')
df_pivot1_1

fig, axes = plt.subplots(figsize=(10,8))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot1_1, cmap='rainbow', ax=axes, annot=True, fmt='.1f')
plt.xlabel('Educational Level')
plt.ylabel('Knowledge Domain')
plt.title('Correlation between Educational Level and Knowledge Domain')
plt.show()

# 이대로도 분명 확인은 가능하지만 좀 더 명확하게 나누어서 보고 싶어서 위의 코드의 일부인 코드 부분에 설정을 주어서 경계선을 추가보겠습니다. 
fig, axes = plt.subplots(figsize=(10,8))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot1_1, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5
)   # linewidths=.5 : 경계선 뚜렷하게 만들어줌
# 글씨 크기 설정 가능
# annot_kws={"size": 20} 추가
# sns.heatmap(df_pivot1_1, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5, annot_kws={"size": 20})

plt.xlabel('Educational Level')
plt.ylabel('Knowledge Domain')
plt.title('Correlation between Educational Level and Knowledge Domain')
plt.show()

# 일부 레이아웃만 없애기
# plt.gca().spines[라벨].set_visible(False)로 레이아웃 일부만 없앨 수 있다.
# spines의 대괄호에 들어갈 수 있는 라벨은 ['right', 'left', 'top', 'bottom']이다.
# 리스트로 받아들여서 한꺼번에 다 되면 좋겠지만 한 개씩만 적용되므로 일일이 입력해야하는 번거로움이 있다.
fig, axes = plt.subplots(figsize=(10,8))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot1_1, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5
)   # linewidths=.5 : 경계선 뚜렷하게 만들어줌
# 글씨 크기 설정 가능
# annot_kws={"size": 20} 추가
# sns.heatmap(df_pivot1_1, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5, annot_kws={"size": 20})
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.xlabel('Educational Level')
plt.ylabel('Knowledge Domain')
plt.title('Correlation between Educational Level and Knowledge Domain\n', fontsize=16)
plt.show()


## 피벗 테이블 만든 후 시각화하기(1) - index 하나만 지정 ##
# aggfung속성을 'count'로 설정하여 각 (x,y)위치의 데이터의 규모(갯수)를 heatmap그래프로 출력한다. 


# Subject & Educational Level
df_pivot1_2 = df.pivot_table(columns=['Educational Level'], index=['Subject'], values='Subject_Num',
                            aggfunc='count')
df_pivot1_2

fig, axes = plt.subplots(figsize=(10,8))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot1_2, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5
)
plt.xlabel('Educational Level')
plt.ylabel('Subject')
plt.title('Correlation between Educational Level and Subject\n', fontsize=16)
plt.show()

# Subject(2D) & Educational Level
df_pivot1_3 = df.pivot_table(columns=['Educational Level'], index=['Subject(2D)'], values='Subject(2D)_Num', aggfunc='count')
df_pivot1_3

fig, axes = plt.subplots(figsize=(10,8))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot1_3, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5
)
plt.xlabel('Educational Level')
plt.ylabel('Subject(2D)')
# y축 회전하기
plt.yticks(rotation=0) ## y label 회전하지 않음
plt.title('Correlation between Educational Level and Subject(2D)\n', fontsize=16)
plt.show()

# VR technology used & Mission_1
df_pivot2_1 = df.pivot_table(columns=['VR technology used'], index=['Mission (Quest/Task)'], values='Mission (Quest/Task)_Num', aggfunc='count')
df_pivot2_1

# NaN 결측치 0으로 채우기
df_pivot2_1 = df_pivot2_1.fillna(0)

fig, axes = plt.subplots(figsize=(4,8))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot2_1, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5
)
plt.xlabel('VR technology used')
plt.ylabel('Mission (Quest/Task)')
# y축 회전하기
plt.yticks(rotation=0) ## y label 회전하지 않기
# x축 회전하기
plt.xticks(rotation=0) ## x label 회전하지 않기 --> figsize 늘리기
plt.title('Correlation between VR technology used and Mission (Quest/Task)\n', fontsize=16)
plt.show()

# VR technology used & Mission_2
df_pivot2_2 = df.pivot_table(columns=['Mission (Quest/Task)'], index=['VR technology used'],
                             values='Mission (Quest/Task)_Num', aggfunc='count')
df_pivot2_2
# NaN 결측치 0으로 채우기
df_pivot2_2 = df_pivot2_2.fillna(0)
fig, axes = plt.subplots(figsize=(12, 3))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot2_2, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5
            )
plt.xlabel('Mission (Quest/Task)')
plt.ylabel('VR technology used')
# y축 회전하기
plt.yticks(rotation=0)  ## y label 회전하지 않기
# x축 회전하기
plt.xticks(rotation=0)  ## x label 회전하지 않기 --> figsize 늘리기
plt.title('Correlation between Mission (Quest/Task) and VR technology used\n', fontsize=16)
plt.show()

# Misson & Cover story

df_pivot2_3 = df.pivot_table(columns=['Mission (Quest/Task)'], index=['Cover Story (Unit : piece(s))'], values='Cover_story_Num',aggfunc='count')
df_pivot2_3

# 이대로도 분명 확인은 가능하지만 좀 더 명확하게 나누어서 보고 싶어서 위의 코드의 일부인 코드 부분에 설정을 주어서 경계선을 추가보겠습니다. 
fig, axes = plt.subplots(figsize=(8, 3))
# annot=True 일때 자리수 지정 ex) fmt='.2f' 소수점 2자리 
sns.heatmap(df_pivot2_3, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5)  # linewidths=.5 : 경계선 뚜렷하게 만들어줌
# 글씨 크기 설정 가능
# annot_kws={"size": 20} 추가
# sns.heatmap(df_pivot1_1, cmap='rainbow', ax=axes, annot=True, fmt='.1f', linewidths=.5, annot_kws={"size": 20})

# y축 회전하기
plt.yticks(rotation=0) ## y label 회전하지 않기
# x축 회전하기
plt.xticks(rotation=75) ## x label 회전하지 않기 --> figsize 늘리기

plt.xlabel('Mission (Quest/Task)')
plt.ylabel('Cover Story (Unit : piece(s))')
plt.title('Correlation between Mission (Quest/Task) and Cover Story (Context)\n', fontsize=15)
plt.show()