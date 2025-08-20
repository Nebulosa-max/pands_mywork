# Q2 — use describe() and show its type
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

desc = df.describe()
print(desc)
print(type(desc))