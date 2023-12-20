def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Contact {e.args[0]} not found."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Insufficient information provided."
    return wrapper


@input_error
def saving(data, dict_user):
    if len(data) == 2 and data[0].isalpha():
        name, phone = data
        dict_user[name] = phone
        return f"Contact added."

@input_error
def change_phone_number(data, dict_user):
    if len(data) == 2:
        name, new_phone = data
        dict_user[name] = new_phone
        return f"Phone number updated."

@input_error
def show_phone_number(data, dict_user):
    name = ' '.join(data)
    if name in dict_user:
        return f"Phone number for {name}: {dict_user[name]}"

def show_all(dict_user):
    if dict_user:
        return '\n'.join([f"{name}: {phone}" for name, phone in dict_user.items()])
    else:
        return "No contacts available."

def hello():
    return "How can I help you?"

def good_bye():
    return "Good bye!"


def commands():
    return {
        'hello': hello,
        'add': saving,
        'change': change_phone_number,
        'phone': show_phone_number,
        'show': show_all,
        'good': good_bye,
        'close': good_bye,
        'exit': good_bye
    }


def handle_command(command, dict_user):
    parts = command.split()
    action = parts[0]

    if len(parts) > 1 and action in ['add', 'change', 'phone']:
        try:
            data = parts[1:]
            if action == 'add':
                return commands()[action](data, dict_user)
            elif action == 'change':
                return commands()[action](data, dict_user)
            elif action == 'phone':
                return commands()[action](data, dict_user)
        except ValueError as e:
            return str(e)
    else:
        if action in commands():
            return commands()[action]()
        elif action == 'show' and len(parts) == 2 and parts[1] == 'all':
            return commands()['show'](dict_user)
        else:
            return "Sorry, I didn't understand your request."


def main():
    dict_user = {}

    while True:
        question = input('>> ').lower().strip()
        result = handle_command(question, dict_user)
        print(result)
        if result == "Good bye!":
            break 

if __name__ == '__main__':
    main()
