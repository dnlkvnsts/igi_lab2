

from base.output import output_in_task4
from base.input import repeat_task


def decorator_it(func):
    def new_function(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        print(f"Positional arguments: {args}")
        print(f"Key arguments: {kwargs}")
        result=func(*args, **kwargs)
        print(f"Result =  {result}")
        return result
    return new_function


def decorator_count(func):
    total=0
    def new_function(*args, **kwargs):
        nonlocal total
        total += 1
        result=func(*args, **kwargs)
        print(f"Number of calls = {total}\n")
        return result
    return new_function



@decorator_count
@decorator_it
def find_amount_of_words_start_with_consonant(words_in_text):
    amount_of_words_start_with_consonant=0
   
    vowels="aeiouy"
    
    for word in words_in_text:
        first_char=word[0].lower()
        if first_char not in vowels and first_char.isalpha():
            amount_of_words_start_with_consonant += 1
    return amount_of_words_start_with_consonant
    
    



def find_words_with_two_consecutive_letter_with_their_order(words_in_text): 
    
    words_with_two_consecutive_letter_with_their_order=[]
   
    for index, word in enumerate(words_in_text, 1):
        low_word=word.lower()
        for i in range(len(low_word)-1):
            if low_word[i] == low_word[i+1]:
                words_with_two_consecutive_letter_with_their_order.append((index, word))    
                break 
    return words_with_two_consecutive_letter_with_their_order



def sort_words_in_alphabetical_order(words_in_text):
   
    
    words_in_alphabetical_order=sorted(words_in_text, key=lambda x: x.lower())
    
    
    return words_in_alphabetical_order
    


def run_task4():
    while True:
        text="So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
        clean_text=text.replace(",","").replace(".","")
        words_in_text=clean_text.split()
    
    
        amount_of_words_start_with_consonant=find_amount_of_words_start_with_consonant(words_in_text)
        words_with_two_consecutive_letter_with_their_order=find_words_with_two_consecutive_letter_with_their_order(words_in_text)
        words_in_alphabetical_order=sort_words_in_alphabetical_order(words_in_text)
    
    
        output_in_task4(text, amount_of_words_start_with_consonant, words_with_two_consecutive_letter_with_their_order, words_in_alphabetical_order)
        if not repeat_task():
            break