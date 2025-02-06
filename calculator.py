
# Functions with operations
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    if y == 0:
        return "Error, Division by zero!"
    return x / y


# Function main 
def main():
    print("This is SIMPLE CALCULATOR PROJECT, made my tevoshw, 06/02/2025\n\n\n")
    print("""Select Operation you will do
          
          1 - Add
          2 - Subtract
          3 - Multiply
          4 - Divide
          
           \n\n""") 
    
    # Loop for user choose
    while True:
        choose_operation = int(input("\n\nWhat's option you will choose?: "))
        if choose_operation in [1, 2 , 3, 4]:
            first_number = float(input("\nEnter the first number: "))
            second_numner = float(input("Enter the second number: "))

        match choose_operation:
            case 1:
                print(f"The add of {first_number} + {second_numner} = {add(first_number, second_numner)}")
            case 2:
                print(f"The sub of {first_number} - {second_numner} = {subtract(first_number, second_numner)}")
            case 3:
                print(f"The multiply of {first_number} * {second_numner} = {multiply(first_number, second_numner):.3f}")
            case 4:
                print(f"The divion of {first_number} - {second_numner} = {division(first_number, second_numner):.2f}")
            case _:
                print("That it's invalid option!")
        break

# Call of the function main
main()