# Simple Calculator Program

print("=== SIMPLE CALCULATOR ===")

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display operation choices
print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user choice
choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation based on choice
if choice == "1":
    result = num1 + num2
    print(f"\n✅ Result: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"\n✅ Result: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"\n✅ Result: {num1} × {num2} = {result}")

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"\n✅ Result: {num1} ÷ {num2} = {result}")
    else:
        print("\n❌ Error: Division by zero is not allowed!")

else:
    print("\n❌ Invalid choice! Please select 1, 2, 3, or 4.")
