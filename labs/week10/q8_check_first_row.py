# Q8 — print just the first row (index 0) to check
import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "data"
logFilename = path / "access.log.demo"

df = pd.read_csv(logFilename, sep=' ', header=None)
print(df.iloc[0])