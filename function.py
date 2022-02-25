# Print welcome message for a different persons


def age():
    age_customer = int(input("How old are you? "))
    if age_customer <= 30:
        print("You are so young")
    else:
        print("That is good age")
def welcome():
    name = input("You are a new our friend\nPlease input your name: ")
    print("We are so happy to see you " + name.capitalize())
def ask():
    ask = input("Do you want to proceed? ")
    if ask == "y" and "Y":
        print("Let's continue")
        age()
    else:
        print("It's so sorry")

welcome()
ask()

# declare function sum
def sum(x,y):
    print(x + y)
# give number to function
sum(10,20)