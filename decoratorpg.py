def my_decorator(function):
    def wrapper(str_ing):
        print('decorated')
        function(str_ing)
    return wrapper


@my_decorator
def print_me(str_ing):
    print(str_ing)


print_me('Op')

