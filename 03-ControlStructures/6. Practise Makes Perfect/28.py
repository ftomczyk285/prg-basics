prev_number = 1
more_prev_number = 0
print(more_prev_number, end=' ')
print(prev_number, end=' ')
for i in range(2, 21):
    current_number = prev_number + more_prev_number
    print(current_number, end=' ')
    more_prev_number = prev_number
    prev_number = current_number