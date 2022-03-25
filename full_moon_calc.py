import datetime as dt
from dateutil.relativedelta import relativedelta

moon_phases = [6, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
day_0 = dt.date.fromisoformat('2024-05-16')


def get_phase(input_date: str) -> int:
    """
    Given a date in YYYY-MM-DD format, check what moon phase it is in

    Day 0 is May 17, Year 4
    Day 0 should be Mar 1, 2021
    22 May should return 4
    23 May should return 4
    17 May should return 6
    """

    d = dt.date.fromisoformat(input_date)

    delta = d - day_0
    #print(d)
    #print(delta.days)
    #print(f'looking for index {delta.days % len(moon_phases)}')
    #print(f'phase is {moon_phases[delta.days % len(moon_phases)]}')

    return moon_phases[delta.days % len(moon_phases)]


def get_f_13_days() -> list:
    """
    From Feb 1, Year 1 - Jan 31, Year 4, return all days that are
    Friday the 13th
    """
    fridays = []

    d = dt.date.fromisoformat('2021-02-13')
    end = dt.date.fromisoformat('2025-01-31')
    while d < end:
        if d.weekday() == 4:
            fridays.append(d.isoformat())
        d = d + relativedelta(months=1)

    return fridays


def main():
    fridays = get_f_13_days()
    for f in fridays:
        if get_phase(f) == 1:
            print(f)


def test_days():
    get_phase('2024-05-17')
    get_phase('2024-05-18')
    get_phase('2024-05-19')
    get_phase('2024-05-20')
    get_phase('2024-05-21')
    get_phase('2024-05-22')


if __name__ == '__main__':
    main()
