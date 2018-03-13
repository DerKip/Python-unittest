

def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    if type (first or last) != str:
        raise TypeError
    full_name = first + ' ' + last
    return full_name.title()



def get_email(first,last):
    '''Generates email'''
    email=first+last+'@company.com'
    return email

# print(get_formatted_name('james','laykan'))