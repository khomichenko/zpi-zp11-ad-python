"""
Файл frogs.csv.
1. Яка середня кількість місць для розмноження жаб?
2. Перевірити чи нормально розподілена висота.
3. Чи є зв’язок між кількістю місць для розмноження та середньою максимальною температурою?
4. Побудувати лінійну регресійну модель залежності кількості можливих груп для розмноження від висоти.
"""
import pandas as pd
import numpy as np
import scipy as scipy

df = pd.read_csv(r'frogs.csv')

# 1
print("1. Яка середня кількість місць для розмноження жаб? ")
print(df['NoOfSites'].mean())

# 2
print("2. Перевірити чи нормально розподілена висота")
shapiroTest = scipy.stats.shapiro(df['altitude'])
if shapiroTest.pvalue < 0.05:
    print("Висота розподілена не нормально (згідно теста Шапіро-Уілка p<0.05, p={})".format(shapiroTest.pvalue))
else:
    print("Висота розподілена нормально (згідно теста Шапіро-Уілка)")
ksTest = scipy.stats.kstest(df['altitude'], 'norm')
if ksTest.pvalue < 0.05:
    print("Висота розподілена не нормально (згідно теста Колмогорова-Смирнова p<0.05, p={})".format(ksTest.pvalue))
else:
    print("Висота розподілена нормально (згідно теста Колмогорова-Смирнова)")

# 3
print("3. Чи є зв’язок між кількістю місць для розмноження та середньою максимальною температурою?")
correlation =scipy.stats.spearmanr(df['NoOfSites'], df['meanmax']).correlation
print("Коефіцієнт кореляції Спірмена {} дуже малий, зв’язок майже відсутній".format(correlation))

# 4
print("4. Побудувати лінійну регресійну модель залежності кількості можливих груп для розмноження від висоти.")
lin = scipy.stats.linregress(df['NoOfPools'], df['altitude'])
print("Y = {} + {} * x".format(lin.intercept, lin.slope))