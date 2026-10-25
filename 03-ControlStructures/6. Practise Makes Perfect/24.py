reverse = False
for i in range(1, 10):
    if reverse:
        print("*" * (10 - i))
    else:
        print("*" * i)
    if i == 5:
        reverse = True