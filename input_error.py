def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def remove_contact(args, contacts):
    name = args[0]
    del contacts[name]
    return "Contact removed."
