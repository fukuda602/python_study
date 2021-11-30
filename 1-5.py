from random import randint
tickets = 5
point = 0
fmt = "{:>3}"

while tickets > 0:
    r = randint(0,20)
    point += r
    print(fmt.format(r))
    tickets -= 1

print("-" * 3)
print(fmt.format(point))


    
