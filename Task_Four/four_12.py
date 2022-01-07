
def fun():
    try:
        5/0
    except ZeroDivisionError:
        print("Can't divisible by zero")
    finally:
        print("exception")
fun()