# Q5 — add describe() to a second sheet named 'summary'
import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "data"
path.mkdir(exist_ok=True)
excelFilename = path / "grades.xlsx"

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

# write/append using ExcelWriter
with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='w') as writer:
    df.to_excel(writer, index=False, sheet_name='data')
    df.describe().to_excel(writer, sheet_name='summary')

print(f"Wrote {excelFilename} with sheets: data, summary")