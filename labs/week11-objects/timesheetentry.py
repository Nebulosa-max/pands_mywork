# labs/week11-objects/timesheetentry.py
import datetime as dt

class Timesheetentry:
    def __init__(self, project: str, start: dt.datetime, duration: int):
        self.project = project
        self.start = start
        self.duration = duration

    def __str__(self) -> str:
        # project ; duration
        return f"{self.project}; {self.duration}"

if __name__ == "__main__":
    ts = Timesheetentry("test", dt.datetime(2021, 3, 19, 16, 20), 60)
    print(ts)  # -> test; 60