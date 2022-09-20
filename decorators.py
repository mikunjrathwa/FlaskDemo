class MyDecorators:
    def __init__(self):
        pass

    def italify(self, func):
        def wrapper():
            return f'<i>{func()}</i>'
        return wrapper
