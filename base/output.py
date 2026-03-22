



def output_in_task1(x, n, fx, math_fx, eps):
    header = f"| {'x':^10} | {'n':^5} | {'F(x)':^15} | {'Math F(x)':^15} | {'eps':^10} |"
    separator = "-" * len(header)
    
    print("\nThe result of the calculations of the first task:")
    print(separator)
    print(header)
    print(separator)
    
    row = f"| {x:^10.5f} | {n:^5} | {fx:^15.6f} | {math_fx:^15.6f} | {eps:^10.1e} |"
    print(row)
    print(separator)
    
      
def output_in_task2(amount_of_numbers, sequence):
    print("\nThe result of the calculations of the second task:")
    print(f"Initial sequence: {sequence}")
    print(f"The amount of numbers less than 10: {amount_of_numbers}")
    
    
def output_in_task3(text, amount_of_digits, amount_of_letters):
    print("\nThe result of the calculations of the third task:")
    print(f"Original text: {text}")
    print(f"1.Amount of digits: {amount_of_digits}")
    print(f"2.Amount of letters: {amount_of_letters}")


def output_in_task4(text, amount_of_words_start_with_consonant, words_with_two_consecutive_letter_with_their_order, words_in_alphabetical_order):
    print("\nThe result of the calculations of the fourth task:")
    print(f"Original text:\n {text}\n")
    print(f"1.Amount of words start with consonant: {amount_of_words_start_with_consonant}")
    print(f"2.Words with two consecutive letter with their order: {words_with_two_consecutive_letter_with_their_order}")
    print(f"3.Words in alphabetical order {words_in_alphabetical_order}\n")
    
    
def output_in_task5(number_collection, amount_of_numbers_grater_than_c, mul_elements):
    print("\nThe result of the calculations of the fifth task:")
    print(f"1.Number collection {number_collection}")
    print(f"2.Amount of numbers grater than c: {amount_of_numbers_grater_than_c}")
    if mul_elements is None:
        print("3. Mul of elements are after max(abs) element: No elements after max(abs)!")
    else:
        print(f"3.Mul of elements are after max(abs) element: {mul_elements}")
     