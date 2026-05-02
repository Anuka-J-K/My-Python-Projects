try:
    birth_year = int(input("Enter your year of birth: "))
    future_year = int(input("Enter a future year: "))

    if birth_year < 0 or future_year < 0:
        print("Years cannot be negative.")
    elif future_year <= birth_year:
        print("Future year must be greater than birth year.")
    else:
        age = future_year - birth_year
        print("Your age in", future_year, "will be:", age)

except ValueError:
    print("Please enter valid numeric values.")

