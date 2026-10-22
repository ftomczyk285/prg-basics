###
# A program that checks if an entered name is a female name
#
name = input('Enter a name: ')
if name[len(name)-1] == 'a':
    print(f'{name} -- Polish female name')