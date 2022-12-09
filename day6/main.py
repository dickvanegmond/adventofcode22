with open('day6/input.txt') as f:
    lines = f.read().splitlines() 

stream = lines[0]

# Answer part 1 
for i in range(len(stream)):
    if len(set(stream[i:i+4])) > 3:
        print("EUREKA")
        print(i+4)
        break

for i in range(len(stream)):
    if len(set(stream[i:i+14])) > 13:
        print("EUREKA")
        print(i+14)
        break
