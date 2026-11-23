# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# Calculates expenses
food_expenses = 0
transport_expences = 0
utilities_expenses = 0
total_weekly_expenses = []
for row in monthly_expenses:
    total_weekly_expenses.append(row[0] + row[1] + row[2])
    food_expenses += row[0]
    transport_expences += row[1]
    utilities_expenses += row[2]

total_expenses = 0
for week in total_weekly_expenses:
    total_expenses += week

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_expenses)
print('Transport:', transport_expences)
print('Utilities:', utilities_expenses)
print('Week 1:', total_weekly_expenses[0])
print('Week 2:', total_weekly_expenses[1])
print('Week 3:', total_weekly_expenses[2])
print('Week 4:', total_weekly_expenses[3])
print('---------------')
print('TOTAL:', total_expenses)