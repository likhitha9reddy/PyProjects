#for loop

print("For Loop")
numbers = [1,2,3,4]

for item in numbers:
    print("The number is",item)

print()
#while loop

print("While Loop")
run = True
current = 1

while run:
    if current == 100:
        run = False
        print(current)
    else:
        current += 1
        print(current)
