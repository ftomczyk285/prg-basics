###
# A program that calculates a dog's age in dog's years
#
dog_age = int(input('Enter dog age in human years: '))

if dog_age <= 2:
    dog_age_in_dog_years = dog_age * 10.5
else:
    dog_age_in_dog_years = 21 + (dog_age - 2) * 4

print(f'Dog age in dog years: {dog_age_in_dog_years}')