# DECORATORS taking arguements

def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed after', original_function.__name__)
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with arguements ({},{})'.format(name, age))


display_info('john', 25)
display_info('sam', 30)
