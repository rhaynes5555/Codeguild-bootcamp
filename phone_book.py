# Phonebook creates a dictionary with a key of first name and value of a dictionary of information.

phonebook = {'Ellie': {'name': 'Ellie', 'number': '360-600-1212'},
             'Taylor': {'name': 'Taylor', 'number': '360-600-1313'}}

# Search function searches for the name


def search():
    search = raw_input('seach for name: ')
    try:
        print ('Record found:')
        print ('Name: ' + phonebook[search]['name'])
        print ('Number: ' + phonebook[search]['number'])
    except:
        print ('No entry found')
    phone_book()

def add():
    print ('add an entry:')
    add_name = raw_input('Enter name: ')
    add_number = raw_input('Enter number: ')
    phonebook[add_name] = {'name': add_name, 'number': add_number}
    phone_book()


def delete():
    delete_name = raw_input('Enter name to be Deleted: ')
    try:
        phonebook.pop(delete_name)
    except:
        print ('No entry found')
    phone_book()


def update():
    name = raw_input('Enter the name to be changed: ')
    update_choice = int(raw_input('Press 1 to update name \nPress 2 to update number: '))
    if update_choice == 1:
        new_name = raw_input('Enter the new name: ')
        phonebook[name]['name']=new_name
    elif update_choice == 2:
        new_number = raw_input('Enter the new phone number: ')
        phonebook[name]['number']=new_number
    phone_book()


def phone_book():
    choice = int(raw_input('''
choose:
1 to search
2 to add
3 to delete
4 to update
5 to exit
>'''))
    if choice == 1:
        search()
    elif choice == 2:
        add()
    elif choice == 3:
        delete()
    elif choice == 4:
        update()
    else:
        exit()

phone_book()

