categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

most_expensive_category_index = 0
for i in range(1, len(categories)):
    if expenses[i] > expenses[most_expensive_category_index]:
        most_expensive_category_index = i

print('Most expensive category was', categories[most_expensive_category_index], 'it costed', expenses[most_expensive_category_index])