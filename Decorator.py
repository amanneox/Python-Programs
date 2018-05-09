def my_decorator(some_function):

    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper



@my_decorator
def just_some_function():
    print("Wheee!")


just_some_function()
