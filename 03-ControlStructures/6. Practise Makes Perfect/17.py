time24 = input("Enter time in 24-hour format (HH:MM): ")

if time24[2] != ':':
    time24 = '0' + time24  # Add leading zero if needed

hours = int(time24[:2])
minutes = int(time24[3:])
if hours == 24:
    hours = 0
    print(f"Time in 12-hour format: {hours}:{minutes:02d} AM")
elif hours > 12:
    hours -= 12
    print(f"Time in 12-hour format: {hours}:{minutes:02d} PM")
else:
    print(f"Time in 12-hour format: {hours}:{minutes:02d} AM")