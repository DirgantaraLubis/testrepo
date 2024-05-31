while True:
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. Exit")
    selection = input('Select option to perform: ')
    if selection == "5":
        break
    try: 
        test1 = float(selection)
    except:
        print("Input the right option")
        continue
    test1 = float(selection)
    if test1 > 5:
        print("Input the right option")
        continue
    elif test1 < 1:
        print("Input the right option")
        continue
    a = input('Enter first number: ')
    b = input('Enter second number: ')
    try:
        z = float(a)
    except:
        print('Error, please input the right number')
        continue
    try:
        x = float(b)
    except:
        print('Error, please input the right number')
        continue
    if test1 == 1:
        print("The result is:",z+x)
    elif test1 == 2:
        print("The result is:",z-x)
    elif test1 == 3:
        print("The result is:",z*x)
    elif test1 == 4:
        print("The result is:",z/x)