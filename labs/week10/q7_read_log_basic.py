# Q7 — read access log with space separator, no header
import pandas as pd
from pathlib import Path

path = Path(__file__).parent / "data"
logFilename = path / "access.log.demo"

df = pd.read_csv(logFilename, sep=' ', header=None)
print(df)