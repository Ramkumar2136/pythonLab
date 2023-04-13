try:
    number1,number2= eval(input("Enter two number seprated by a comma : "))
    result= number1/number2
    print("Result is :> ",result)
    if (number1 == 0):
        raise RuntimeError()
except ZeroDivisionError:
    print("Division Not Posible.")
except SyntaxError:
    print("Input missing comma ... ")
except RuntimeError:
    print('Something went worng..')
else:
    print("No exceptions..Whoo!")
finally:
    print("The finally block executed.")