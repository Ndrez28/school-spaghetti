def new_contact_store():
    return []

def add_new_contact(contacts, first_name, last_name,
                    email, phone_number, birthday):
    new_store = [
        first_name,
        last_name,
        email,
        phone_number,
        birthday
    ]
    contacts.append(new_store)
    return contacts

def has_contact(contacts, first_name, last_name):
    for i in range(len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            return True

def get_contact_string(contacts, first_name, last_name):
    for i in range(len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            return(contacts[i][0], contacts[i][1])

def remove_contact(contacts, first_name, last_name):
    for i in range(len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            contacts.pop(i) 
    return contacts

def update_contact_first_name(contacts, first_name, last_name, new_field_value):
    for i in range (len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            contacts[i][0] = new_field_value
    return contacts

def update_contact_last_name(contacts, first_name, last_name, new_field_value):
    for i in range (len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            contacts[i][1] = new_field_value
    return contacts

def update_contact_email(contacts, first_name, last_name, new_field_value):
    for i in range (len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            contacts[i][2] = new_field_value
    return contacts

def update_contact_phone_number(contacts, first_name, last_name, new_field_value):
    for i in range (len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            contacts[i][3] = new_field_value
    return contacts

def update_contact_birthday(contacts,first_name,last_name,new_field_value):
    for i in range (len(contacts)):
        if contacts[i][0] == first_name and contacts[i][1] == last_name:
            contacts[i][4] = new_field_value
    return contacts


