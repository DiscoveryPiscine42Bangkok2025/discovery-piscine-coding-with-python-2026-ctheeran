first_number = int(input("Please enter the first number : "))
second_number = int(input("Please enter the second number : "))

product = first_number * second_number

print(f"{first_number} x {second_number} = {product}")

if product == 0:
    print("The result is zero")
elif product < 0:
    print("The result is negative")
else:
    print("The result is both positive and negative")
