from __future__ import annotations
import datetime as dt
from timesheetentry import Timesheetentry

class Employee:
    # NOTE: the PDF shows `timesheets = []` at class level (don’t do that).
    # We create a new list per instance in __init__ instead.

    def __init__(self, first: str, last: str):
        self.first = first
        self.last = last
        self.timesheets: list[Timesheetentry] = []

    def __str__(self) -> str:
        return self.first + ' ' + self.last

    # 7) logminutes(project, minutes)
    def logminutes(self, project: str, minutes: int, when: dt.datetime | None = None) -> None:
        if when is None:
            when = dt.datetime.now()
        entry = Timesheetentry(project, when, minutes)
        self.timesheets.append(entry)

    # 8) gettotaltime(): total minutes of all entries
    def gettotaltime(self) -> int:
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
        return total_minutes


if __name__ == "__main__":
    test = Employee('some', 'one')
    print(test)                     # -> some one
    assert str(test) == 'some one'
    test.logminutes('p1', 30)
    test.logminutes('p1', 60)
    mins = test.gettotaltime()
    print(mins)                     # -> 90
    assert mins == 90
    print('all good')