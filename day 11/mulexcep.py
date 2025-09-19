try:
    numbers = [10, 20, 30]
    index = int(input("Enter index: "))
    print("Value:", numbers[index])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid input, please enter a number.")