try:
    a=int(input())
    b=int(input())
    c=input()
    print(c/a)
    print(a+b)
    print(d)

except ValueError as e:
    print("Value Error", e)

except TypeError as e:
    print("Type Error",e)

except NameError as e:
    print("Name Error", e)

except Exception as e:
    print("Something went wrong")

finally:
    print("Done")
