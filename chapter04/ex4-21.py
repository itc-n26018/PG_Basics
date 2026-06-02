try:
    a = input("type a number:")
    b = input("tyoe another:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")
