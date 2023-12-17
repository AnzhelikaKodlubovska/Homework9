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
    
def saving(name, phone, dict_user):
    dict_user[name] = phone
    return dict_user
    
def change_phone_number(name, new_phone, dict_user):
    if name in dict_user:
        dict_user[name] = new_phone
    return dict_user

def show_phone_number(name, dict_user):
    if name in dict_user:
        print(f"Phone number for {name}: {dict_user[name]}")
    else:
        print(f"Contact {name} not found.")

def show_all_contacts(dict_user):
    if dict_user:
        for name, phone in dict_user.items():
            print(f"{name}: {phone}")

@input_error
def saving(name, phone, dict_user):
    dict_user[name] = phone
    return dict_user

@input_error
def change_phone_number(name, new_phone, dict_user):
    if name in dict_user:
        dict_user[name] = new_phone
        return f"Phone number for {name} updated."
    else:
        return f"Contact {name} not found."

@input_error
def show_phone_number(name, dict_user):
    if name in dict_user:
        return f"Phone number for {name}: {dict_user[name]}"
    else:
        return f"Contact {name} not found."
              
def main():
    dict_user = {}  
    while True:
        question = input('>> ').lower()
        if question == 'hello':
            print('How can I help you?')
        elif question.startswith('add'):
            data = question.split()[1:]  
            if len(data) == 2:
                name, phone = data
                dict_user = saving(name, phone, dict_user)
            else:
                print("Invalid input format. Please use 'add name phone'.")
        elif question.startswith('change'):
            data = question.split()[1:]  
            if len(data) == 2:
                name, new_phone = data
                dict_user = change_phone_number(name, new_phone, dict_user)
            else:
                print("Invalid input format. Please use 'change name new_phone'.")
        elif question.startswith('phone'):
            name = question.split(' ', 1)[1] 
            show_phone_number(name, dict_user)
        elif question == 'show all':
            show_all_contacts(dict_user)
        elif question == '.' or question == "good bye" or question == "close" or question == "exit":
            break
        else:
            print("Sorry, I didn't understand your request.")
    
if __name__ == '__main__':
    main()
