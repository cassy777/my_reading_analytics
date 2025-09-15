#1.读取数据
import pandas as pd 
df=pd.read_csv('data/reading_data.csv')

#2.返回基本信息
print(df.head())
print(df.info())

#3.简单分析
#总阅读时间--.sum()
total_minutes=df['reading_minutes'].sum()
print(f"总阅读时间为{total_minutes}分钟")#注意print后面加f

#读的最多的书--.groupby().sum().sort_values()
book_stats=df.groupby('book')['reading_minutes'].sum().sort_values(ascending=False)
print('每本书的阅读时长：')
print(book_stats)

#读最久的天
day_stats=df.groupby('date')['reading_minutes'].sum()
max_day=day_stats.idxmax()
print(f"阅读最久的天是{max_day},读了{day_stats[max_day]}分钟")

#4.生成一个html报告





