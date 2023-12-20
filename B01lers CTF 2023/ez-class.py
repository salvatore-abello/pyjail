import shutil

def get_input_validated(validator):
    while True:
        try:
            return validator(input('>> '))
        except EOFError:
            exit()
        except:
            print("Invalid input")

def get_choice(max, min=1):
    def validate(data):
        choice = int(data)
        if not (min <= choice <= max):
            raise ValueError()
        return choice
        
    return get_input_validated(validate)

def get_positive_number():
    def validate(data):
        num = int(data)
        if num < 0:
            raise ValueError()
        return num

    return get_input_validated(validate)

def get_legal_code():
    def validate(data):
        for char in ['(', ')', '.', '\n']:
            if char in data:
                raise ValueError()
        return data

    return get_input_validated(validate)

def write_class():
    print('Enter new class name')
    name = get_legal_code()

    print('Enter parent class to inherit from')
    parent = get_legal_code()

    print('How many methods will this class have')
    method_count = get_positive_number()

    method_code = ''
    for _ in range(method_count):
        print('Enter method name')
        method_name = get_legal_code()

        print('Enter method params')
        params = get_legal_code()

        print('Enter method body')
        body = get_legal_code()

        method_code += f'\tdef {method_name}({params}):\n'
        method_code += '\t\t' + body + '\n'

    if method_count == 0:
        method_code = '\tpass'

    class_str = f'class {name}({parent}):\n'
    class_str += method_code

    with open('/tmp/' + name + '.py', 'w') as f:
        f.write(class_str)

def exec_class(filename, dependancies, class_name):
    for dep in dependancies:
        with open('/tmp/' + dep, 'r') as f:
            exec(f.read())

    with open('/tmp/' + filename, 'r') as f:
        exec(f.read())

    print('Here is an instance of your class')
    print(locals()[class_name]())

def run_class():
    print('Enter class name to run')
    name = input('>> ')

    print('Enter class dependancies seperated by a comma')
    dependancies = filter(lambda a : a != '.py', map(lambda a : a.strip() + '.py', input('>> ').split(',')))

    try:
        exec_class(name + '.py', dependancies, name)
    except FileNotFoundError:
        print('Could not open class or one of its dependancies')


def main():
    print('Welcome to EzClass runner')

    shutil.copy('flag.txt', '/tmp/flag.txt')

    while True:
        print('What you want to do?')
        print('1. Write new class')
        print('2. Run class')
        choice = get_choice(2)
        if choice == 1:
            write_class()
        else:
            run_class()

if __name__ == '__main__':
    main()
