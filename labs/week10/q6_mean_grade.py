# Q6 — calculate and print the mean of the grades
import pandas as pd

listData = [
    ['John', 'math', 23],
    ['John', 'programming', 66],
    ['Mary', 'math', 45],
    ['Mary', 'programming', 33],
    ['Mark', 'SIEM', 57],
    ['Mark', 'programming', 70],
    ['Mark', 'math', 73],
    ['John', 'programming', 61],
]
df = pd.DataFrame(listData, columns=['name', 'subject', 'grade'])

mean_v1 = df.describe().loc['mean', 'grade']
mean_v2 = df['grade'].mean()

print("Mean grade via describe().loc:", mean_v1)
print("Mean grade via Series.mean():  ", mean_v2)