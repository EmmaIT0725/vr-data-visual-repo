import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)

### Pie Chart Visualization ###

# 레이블 인코더 적용하기
from sklearn.preprocessing import LabelEncoder

def apply_label_encoding(df, column_name):
    label_encoder = LabelEncoder()
    label_encoded = label_encoder.fit_transform(df[column_name])
    print(f'레이블 인코딩 적용 후 데이터 ({column_name}): {label_encoded}')
    df.insert(df.columns.get_loc(column_name) + 1, f'{column_name}_Num', label_encoded)

columns_to_encode = ['Subject', 'Subject(2D)', 'Knowledge Domain', 'Mission (Quest/Task)', 'Operation (Activities)', 'Resources', 'Feedback', 'Role']

for column in columns_to_encode:
    apply_label_encoding(df, column)


# Cover story 단위 '개' 삭제하기
## 1. 부분일치
# regex=True 파라미터를 추가함으로써 해당 문자가 포함되어 있으면 문자가 대체된다.

# df.replace('(<|>|\s|희석|확인함)','', regex=True, inplace=True)
# df.replace('(?i).*(fibrin|citrate).*', '', regex=True, inplace=True)
# 참고로 (?i)를 추가하면 대소문자 상관없이 replace를 적용될 수 있다. 

## 2. 완전일치
# regex=True 없이 작성하면 된다. 

# df.replace('.', '', inplace=True)
# df['Cover Story (Context)'].replace('개','', regex=True, inplace=True)
df.replace('nan', 'Not specified', inplace=True)
df.replace('NaN', 'Not specified', inplace=True)


# 산점도 그리기
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(df['Subject(2D)'], df['Subject'])
ax.set_title('Subject(2D)-Subject')
fig.show()

# 메인 그래프에 Subject 산점도 그리기
# fig, ax = plt.subplots(figsize=(10, 8))
sc = ax.scatter(df['Subject(2D)'], df['Subject'],
                linewidths=0.5, edgecolors='k', alpha=1,
                s=((df['Subject_Value_Counts'])+5)**2.5, c=df['Subject_Value_Counts'], cmap='hsv')
# scatter 함수의 매개 변수 s : 도형의 크기 지정
# scatter 함수의 매개 변수 c : 색상 이름 또는 숫자의 연속형
ax.set_title('Correlation between Subject and Subject(2D)')
ax.set_ylabel('Subject')
fig.colorbar(sc)
fig.show()
print(fig.show())

# import pandas as pd
# import numpy as np
# import matplotlib
# import openpyxl
# from sklearn import __version__ as sklearn_version

# print("pandas version:", pd.__version__)
# print("numpy version:", np.__version__)
# print("matplotlib version:", matplotlib.__version__)
# print("openpyxl version:", openpyxl.__version__)
# print("scikit-learn version:", sklearn_version)
