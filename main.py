import datetime as dt
import calendar
import pandas as pd
import functions as mh

MONTHS = [calendar.month_name[i] for i in range(1, 13)]


def create_date_table(start='2000-01-01', end='2050-12-31'):
    start_ts = pd.to_datetime(start).date()
    end_ts = pd.to_datetime(end).date()
    # record timestamp is empty for now
    dates = pd.DataFrame(columns=['Workday'],
                         index=pd.date_range(start_ts, end_ts))
    dates.index.name = 'Date'
    days_names = {
        i: name
        for i, name in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    }
    dates['Day'] = dates.index.dayofweek.map(days_names.get)
    dates['Month'] = dates.index.month
    dates.reset_index(inplace=True)
    dates.index.name = 'date_id'
    return dates


if __name__ == "__main__":
    # grab date
    today = dt.datetime.now()
    year = today.year

    # set calendar df
    calendar = create_date_table(start=f"{today.year}-{today.month}-{today.day}", end=f"{today.year}-12-31")

    # set free days on weekends
    for i in calendar.index:
        if calendar['Day'][i] == "Sunday" or calendar['Day'][i] == 'Saturday':
            calendar.at[i, 'Workday'] = 1
        else:
            calendar.at[i, 'Workday'] = 0

    # set work-free days on holidays
    holidays = [f"{year}-01-01", f"{year}-01-06", f"{year}-05-01", f"{year}-05-03", f"{year}-08-15",
                f"{year}-11-1", f"{year}-11-11", f"{year}-12-25", f"{year}-12-26"]
    holidays_dt = [pd.to_datetime(w, yearfirst=True) for w in holidays]
    # add movable holidays i.e. easter
    holidays_dt.extend(mh.calculate_easter(int(year)))
    # set them to free too.

    for date in holidays_dt:
        if date in calendar['Date'].values:
            # grabbing index returns index datatype, getting its value returns a list, need to get first item of it.
            a = calendar.index[calendar['Date'] == date].values[0]
            calendar.at[a, 'Workday'] = 0
