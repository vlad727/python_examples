name = input("Please input your name: ")
print(name)

x = int(input("Please input first number: "))
y = int(input("Please input second number: "))
sum = x + y
print(sum)


code = ""

while code != 4312:
    code = int(input("Please input your short code: "))
    print("Access is prohibited, please try again: ")
    if code == 4312:
        print("Welcome")
