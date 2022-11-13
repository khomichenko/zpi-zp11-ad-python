"""
Файл Stars.csv.

1. Побудувати стовпчикові діаграми, на яких відобразити
а) кількість зірок різного кольору;
б) медіанну температуру зірок різного кольору;
в) середній радіус зірок різного кольору з розподілом за типом зірки.

2. Побудувати гістограму температури, загальну і в залежності від спектрального класу.

3. Побудувати діаграму розмаху світності (загальну і в залежності від кольору), визначити чи присутні викиди.

4. За допомогою діаграм розсіювання зробити висновки щодо залежності між
а) температурою і абсолютною величиною;
б) радіусом та температурою.
Порахувати коефіцієнт кореляції за допомогою відповідних функцій.
"""
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

df = pd.read_csv(r'Stars.csv')
df['Color'] = df['Color'].str.lower()
df['Color'] = df['Color'].str.replace('whitish', 'white')
df['Color'] = df['Color'].str.replace('yellowish', 'yellow')
df['Color'] = df['Color'].str.replace('-', ' ')
df['Color'] = df['Color'].str.replace('white yellow', 'yellow white')
df['Color'] = df['Color'].str.replace('white blue', 'blue white')
df['Color'] = df['Color'].str.replace(' white', '')
df['Color'] = df['Color'].str.replace('orange red', 'red')
df['Color'] = df['Color'].str.replace('pale yellow orange', 'orange')

# 1 Побудувати стовпчикові діаграми, на яких відобразити
# df['Color'].value_counts().sort_index().plot.bar(title="1.a. Кількість зірок різного кольору")
# plt.show()
# df[['Color', 'Temperature']].groupby('Color')['Temperature'].mean().plot.bar(title="1.б. Медіанна температуру зірок різного кольору")
# plt.show()
# df[['Color', 'Spectral_Class', 'R']].groupby(['Color', 'Spectral_Class']).mean().plot.bar(title="1.в. середній радіус зірок різного кольору з розподілом за типом зірки.")
# plt.show()

# 2 Побудувати гістограму температури, загальну і в залежності від спектрального класу.
# plt.hist(df['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature')])
# plt.show()
# plt.hist(df.loc[df['Spectral_Class'] == 'A']['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature for the Spectral Class A')])
# plt.show()
# plt.hist(df.loc[df['Spectral_Class'] == 'B']['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature for the Spectral Class B')])
# plt.show()
# plt.hist(df.loc[df['Spectral_Class'] == 'F']['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature for the Spectral Class F')])
# plt.show()
# plt.hist(df.loc[df['Spectral_Class'] == 'G']['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature for the Spectral Class G')])
# plt.show()
# plt.hist(df.loc[df['Spectral_Class'] == 'K']['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature for the Spectral Class K')])
# plt.show()
# plt.hist(df.loc[df['Spectral_Class'] == 'M']['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature for the Spectral Class M')])
# plt.show()
# plt.hist(df.loc[df['Spectral_Class'] == 'O']['Temperature'], color='green', edgecolor='black')
# plt.legend(handles=[matplotlib.patches.Patch(color='green', label='Temperature for the Spectral Class O')])
# plt.show()

# 3 Побудувати діаграму розмаху світності (загальну і в залежності від кольору), визначити чи присутні викиди.
# fig1, ax1 = plt.subplots()
# ax1.set_title('Діаграма розмаху світності')
# ax1.boxplot(df['L'])
# plt.show()
# data = [df['L'],
#        df.loc[df['Color'] == 'red']['L'],
#        df.loc[df['Color'] == 'white']['L'],
#        df.loc[df['Color'] == 'blue']['L'],
#        df.loc[df['Color'] == 'orange']['L']
#        ]
# fig7, ax7 = plt.subplots()
# ax7.set_title('Загальна, red, white, blue, orange')
# ax7.boxplot(data)
# plt.show()

# 4 За допомогою діаграм розсіювання зробити висновки щодо залежності між
# а) температурою і абсолютною величиною;
# б) радіусом та температурою.
# Порахувати коефіцієнт кореляції за допомогою відповідних функцій.
# df.plot.scatter(x='Temperature', y='A_M', title='залежності між температурою і абсолютною величиною')
# plt.show()
# correlation =scipy.stats.spearmanr(df['Temperature'], df['A_M']).correlation
# print("Коефіцієнт кореляції Спірмена {}, зв’язок монотонний".format(correlation))
# df.plot.scatter(x='Temperature', y='R', title='залежності між радіусом та температурою')
# plt.show()
# correlation =scipy.stats.spearmanr(df['Temperature'], df['R']).correlation
# print("Коефіцієнт кореляції Спірмена {}, зв’язок майже відсутній".format(correlation))
