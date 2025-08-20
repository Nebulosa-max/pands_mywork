# Q9 — read the same log but with meaningful column names
import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "data"
logFilename = path / "access.log.demo"

colNames = (
    'ip',
    'dash1',
    'userId',
    'time',
    'url',
    'status code',
    'size of response',
    'referer',
    'user agent',
    'dunno',        # matches the tutor’s example
)

df = pd.read_csv(logFilename, sep=' ', header=None, names=colNames)
print(df.head())
print(df.columns.tolist())