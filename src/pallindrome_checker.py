def pallindrome_checker(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    if cleaned_string == cleaned_string[::-1]:
        return True
    else:
        return False