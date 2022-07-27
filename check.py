def time_converter(time):
    h, m = map(int, time.split(':'))
    print((h-1)%12+1)
    return f"{(h-1)%12+1}:{m:02d} {'ap'[h>11]}.m."


print(time_converter('13:00'))