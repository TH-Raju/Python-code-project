# Here we create a leap Year Programe with python
# you can use it for check leap year


input_year = int(input("Please Enter a Year: "))
if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print("Yes! This is a leap year")
        else:
            print("No! It's not a leap year")
    else:
        print("Yes! This is a leap year")
else:
    print("No! It's not a leap year")