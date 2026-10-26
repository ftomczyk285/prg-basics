def time_string(hours, minutes, time_format):
    minutes = '0' + str(minutes) if minutes < 10 else minutes
    if time_format == '12':
        if hours == 0:
            hours = 12
            return f'{hours}:{minutes}am'
        elif hours > 12:
            hours -= 12
            return f'{hours}:{minutes}pm'
        elif hours == 12:
            return f'{hours}:{minutes}pm'
        else:
            return f'{hours}:{minutes}am'
    elif time_format == '24':
        hours = '0' + str(hours) if hours < 10 else hours
        return f'{hours}:{minutes}'
    else:
        return 'Unknown time format'

print(f'time_string(15, 38, "24") returns "{time_string(15,38, '24')}"')
print(f'time_string(8, 3, "24") returns "{time_string(8, 3, '24')}"')
print(f'time_string(0, 5, "24") returns "{time_string(0, 5, '24')}"')
print(f'time_string(11, 15, "12") returns "{time_string(11, 15, '12')}"')
print(f'time_string(0, 7, "12") returns "{time_string(0, 7, '12')}"')
print(f'time_string(7, 30, "12") returns "{time_string(7, 30, '12')}"')
print(f'time_string(12, 46, "12") returns "{time_string(12, 46, '12')}"')
print(f'time_string(13, 10, "12")) returns "{time_string(13, 10, '12')}"')
print(f'time_string(19, 02, "12") returns "{time_string(19, 2, '12')}"')