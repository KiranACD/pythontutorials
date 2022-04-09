from html import escape
# from htmlize import htmlize_fn

def html_escape(arg):
    return escape(str(arg))

def html_int(arg):
    return f'{arg}(<i>{hex(arg)}</i>)'

def html_real(arg):
    return f'{round(arg, 2)}'

def html_str(arg):
    return html_escape(arg).replace('\n', '<br/>\n')

def html_list(arg):
    items = (f'<li>{htmlize_fn(item)}</li' for item in arg)

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(arg):
    items = (f'<li>{html_escape(k)} = {htmlize_fn(v)}</li>' for k,v in arg.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def htmlize_fn(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, float):
        return html_real(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)

if __name__ == '__main__':
    print(html_str('''This is a multi-line string. It has a special character showing 1 < 2.
    Great work!'''))

    print(html_int(100))

    print(html_real(2.598877))

    print(html_list([1, 2, 3, 4]))

    print()

    print('htmlize')

    print(htmlize_fn(100))
    print(htmlize_fn(['python', (100, 200, 300), 3.5676]))