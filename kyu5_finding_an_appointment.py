def get_start_time(schedules, duration):
    start_time = convert_time('09:00')
    end_time = convert_time('19:00')
    slots = [[start_time + i, start_time + duration + i]
             for i in range(0, end_time - start_time - duration + 1)]
    taken_slots = convert_schedules(schedules)
    for slot in slots:
        if possible(slot, taken_slots):
            [start, _] = slot
            return int_to_time(start)
    return None


def possible(slot, taken_slots):
    for taken in taken_slots:
        if overlapping_range(slot, taken):
            return False
    return True


def overlapping_range(range1, range2):
    [start1, end1] = range1
    [start2, end2] = range2
    if start1 <= start2:
        return end1 > start2
    else:
        return overlapping_range(range2, range1)


def convert_time(timestr):
    [hourstr, minutestr] = timestr.split(':')
    hour = int(hourstr)
    minute = int(minutestr)
    return hour * 60 + minute


def int_to_time(n):
    minute = n % 60
    hour = (n - minute) // 60
    return '{:02d}'.format(hour) + ':' + '{:02d}'.format(minute)


def convert_schedules(schedules):
    converted_schedules = [convert_schedule(s) for s in schedules]
    return [slot
            for schedule in converted_schedules
            for slot in schedule]


def convert_schedule(schedule):
    converted_schedule = []
    for block in schedule:
        [start, end] = block
        converted_schedule.append(
            [convert_time(start), convert_time(end)])
    return converted_schedule


def clever_get_start_time(schedules, duration):
    periods = sorted(sum(schedules, [['19:00', '19:00']]))
    time = '09:00'
    for period in periods:
        if mins(period[0]) >= mins(time) + duration:
            return time
        time = max(time, period[1])
    return None


def mins(timeStr):
    h, m = map(int, timeStr.split(':'))
    return h * 60 + m
