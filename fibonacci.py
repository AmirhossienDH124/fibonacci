# input sequence size
user_sequence_size_input = int(input("Please insert the sequence size: "))
# creat fibonacci function
def fibonacci_function(sequence_size):
    fibonacci_list = []
    while len(fibonacci_list) < sequence_size:
        # appending the first two members [1, 1]
        if len(fibonacci_list) <= 1:
            fibonacci_list.append(1)
            print(fibonacci_list)
        else:
            # appending the other members
            append_item = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(append_item)
            print(fibonacci_list)
    # end of function
    print("\nDone!")
# apply the function
fibonacci_function(user_sequence_size_input)
