from html import escape

def singledispatch(fn):

    registry = {}
    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    decorated.register = register

    return decorated

@singledispatch
def htmlize(arg):
    return escape(str(arg))

@htmlize.register(int)
def html_int(arg):
    return f'{arg}(<i>{hex(arg)}</i>)'

@htmlize.register(list)
@htmlize.register(tuple)
def html_sequence(arg):
    items = (f'<li>{htmlize(item)}</li>' for item in arg)
    return '<ul>\n' + '\n'.join(items) + '\n</ul'

if __name__ == '__main__':
    print(htmlize(100))
    print(htmlize([1,2,3]))
    print(htmlize(['python', (1,2,3), 4]))
