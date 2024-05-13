import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

df = pd.read_excel('./input/데이터 가공 최종_레이블인코딩.xlsx')
print(df)

# Pair plot

# Set style
sns.set_style('whitegrid')

# Pair Plot for Knowledge Domain and Subject
sns.pairplot(df, x_vars=['Knowledge Domain'], y_vars=['Subject'], height=5, aspect=1.5)
plt.title('The Correlation of Knowledge Domain and Subject', fontsize=12)

# Pair Plot for Knowledge Domain and Subject(2D)
sns.pairplot(df, x_vars=['Knowledge Domain'], y_vars=['Subject(2D)'], height=5, aspect=1.5)
plt.title('The Correlation of Knowledge Domain and Subject(2D)', fontsize=12)

# Pair Plot for Educational Level and Knowledge Domain
sns.pairplot(df, x_vars=['Educational Level'], y_vars=['Knowledge Domain'], height=5, aspect=1.5)
plt.title('The Correlation of Educational Level and Knowledge Domain', fontsize=12)

# Pair Plot for Educational Level and Subject
sns.pairplot(df, x_vars=['Educational Level'], y_vars=['Subject'], height=5, aspect=1.5)
plt.title('The Correlation of Educational Level and Subject', fontsize=12)

# Pair Plot for Educational Level and Subject(2D)
sns.pairplot(df, x_vars=['Educational Level'], y_vars=['Subject(2D)'], height=5, aspect=1.5)
plt.title('The Correlation of Educational Level and Subject(2D)', fontsize=12)

plt.show()
