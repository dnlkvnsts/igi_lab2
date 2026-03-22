import base.validation as val 

import random
import string


def input_in_task1():
    
    x=val.get_float_input("Input x:\n")

    eps=val.get_float_positive_input("\nInput eps:\n")

    return x, eps



def initialize_by_user(original_sequence):
    
    sequence = []
    
    for i in original_sequence:
        el=val.get_int_input(f"Input {i+1} integer element\n")
        sequence.append(el)
        
        if el == 100:
            break
        
    return sequence


def initialize_by_function_of_generator(original_sequence):
    
    for _ in original_sequence:
        el=random.randint(0, 150)
        yield el
        
        if el == 100:
            break



def initialize_float_numbers_by_user(original_sequence):
    
    sequence = []
    
    for i in original_sequence:
        el=val.get_float_input(f"Input {i+1} float element\n")
        sequence.append(el)
    return sequence
    
        
        
        
def initialize_with_float_numbers_by_function_of_generator(original_sequence):
    
    for _ in original_sequence:
        el=random.uniform(-500.0, 500.0)
        yield round(el, 2)
    
    
def initialize_string_by_generator(original_sequence):
    """
    Генерирует случайные символы для создания строки.
    """
    
    characters = string.ascii_letters + string.digits + string.punctuation + " "
    
    for _ in original_sequence:
        yield random.choice(characters)
    
def repeat_task():
    while True:
            choice = input("Repeat this task ?(y/n) ").lower()
            if choice == "y":
                return True
            elif choice == "n":
                return False
            else:
                print("Invalid input!!! Input y or n\n")
    