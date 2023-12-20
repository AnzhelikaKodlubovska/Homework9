def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid user name."
        except ValueError:
            return "Invalid input. Please provide correct data."
        except IndexError:
            return "Insufficient information provided."
    return wrapper
    
@input_error
def saving(name, phone, dict_user):
    if name not in dict_user:
        dict_user[name] = phone
        return f"Contact {name} added."
    else:
        return f"Contact {name} already exists. Use 'change' command to update the phone number."

@input_error
def change_phone_number(name, new_phone, dict_user):
    if name in dict_user:
        dict_user[name] = new_phone
        return f"Phone number for {name} updated."
    else:
        return f"Contact {name} not found. Use 'add' command to create a new contact."

@input_error
def show_phone_number(name, dict_user):
    if name in dict_user:
        return f"Phone number for {name}: {dict_user[name]}"
    else:
        return f"Contact {name} not found."
              
def main():
    dict_user = {}  
    while True:
        question = input('>> ').lower().strip()

        known_commands = ['hello', 'add', 'change', 'phone', 'show all', '.', 'good bye', 'close', 'exit']
        command = question.split()[0] if question else ''
        
        if command in known_commands or question == 'show all': 
            commands = {
                'hello': lambda: print('How can I help you?'),
                'add': lambda data: saving(data[0], data[1], dict_user) if len(data) == 2 and data[0].isalpha() else print("Invalid input format. Please use 'add name phone'."),
                'change': lambda data: change_phone_number(data[0], data[1], dict_user) if len(data) == 2 and data[0] in dict_user else print("Contact not found. Use 'add' command to create a new contact."),
                'phone': lambda data: print(show_phone_number(' '.join(data), dict_user)) if ' '.join(data) in dict_user else print(f"Contact {' '.join(data)} not found."),
                'show all': lambda: [print(f"{name}: {phone}") for name, phone in dict_user.items()] if dict_user else print("No contacts available."),
                '.': lambda: (print('Good bye!'), exit()),
                'good bye': lambda: (print('Good bye!'), exit()),
                'close': lambda: (print('Good bye!'), exit()),
                'exit': lambda: (print('Good bye!'), exit()),
            }

            try: 
            
                if command.startswith('add'):
                    data = question.split()[1:]
                    commands['add'](data)
                elif command.startswith('change'):
                    data = question.split()[1:]
                    commands['change'](data)
                elif command.startswith('phone'):
                    data = question.split()[1:]
                    commands['phone'](data)
                elif command in commands:
                    commands[command]()
                elif question == 'show all':  
                    commands['show all']()
                else:
                    print("Sorry, I didn't understand your request.")
            except IndexError:
                print("Insufficient information provided. Try again")
                
        else:
            print("Invalid command. Please enter a valid command.")
    
if __name__ == '__main__':
    main()
