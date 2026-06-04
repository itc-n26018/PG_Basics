def to_float(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string")

c = to_float("9")
print(c)
