with open('day1/input.txt') as f:
    lines = f.read().splitlines() 

# split into meals per elf
mealsPerElf = []
meals = []
for line in lines:
    if not line:
        mealsPerElf.append(meals)
        meals = []
    else:
        meals.append(int(line))

sumOfMealsPerElf = []
for elf in mealsPerElf:
    sumOfMealsPerElf.append(sum(elf))

# Answer to part 1:
print(max(sumOfMealsPerElf))

# Answer to part 2:
sumOfMealsPerElf.sort(reverse=True)
print(sum(sumOfMealsPerElf[0:3]))