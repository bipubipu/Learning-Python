from operator import add


def add_time(start, duration, start_day=None):
    DAYS = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_time = time_split(start[:5])
    duration_time = time_split(duration)
    start_is_AM = True if 'AM' in start else False
    final_time = list(map(add, start_time, duration_time))

    if final_time[1] > 60:
        final_time[1] -= 60
        final_time[0] += 1

    days_later = final_time[0]//24
    final_time[0] %= 24

    if final_time[0] >= 12:
        start_is_AM = not start_is_AM
        if start_is_AM:
            days_later += 1
    if final_time[0] > 12:
        final_time[0] -= 12

    if start_is_AM and final_time[0] == 0:
        final_time[0] = 12
    final_output = f'{final_time[0]}:{final_time[1]:02d} '
    final_output += 'AM' if start_is_AM else 'PM'

    if start_day:
        start_day = start_day.lower().capitalize()
        final_day = DAYS[(DAYS.index(start_day) + days_later) % 7]
        final_output += ', ' + final_day

    if days_later == 1:
        final_output += ' (next day)'
    elif days_later > 1:
        final_output += f' ({days_later} days later)'

    return final_output


def time_split(time):
    time = time.split(':')
    return [int(time[0]), int(time[1])]
