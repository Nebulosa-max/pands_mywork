# Q3 — write the DataFrame to CSV
import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "data"
path.mkdir(exist_ok=True)
csvFilename = path / "grades.csv"

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
df.to_csv(csvFilename, index=False)
print(f"Wrote {csvFilename}")