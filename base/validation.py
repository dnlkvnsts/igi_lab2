


def get_float_input(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            
            
def get_int_input(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Invalid input. Please enter an integer number.\n")
            
            
def get_float_positive_input(text):
    
    while True:
        number=get_float_input(text)
        if 0 < number < 1:
            return number
        else:
            print("Invalid input. Please enter a positive float number from 0 to 1.\n")

def get_string(message):
    while True:
        text=input(message)
    
        if text.strip():
            return text
    
        print("Invalid input. The string cannot be empty or consist only of spaces.\n")