# TASK 6: File Handling and Metaprogramming 
# implement metaprogramming techniques to dynamically generate function names 
# for pytest test cases based on the filenames of the text files 

# read from task6_read_me.txt and count the number of words in the file 
file_name = "task6_read_me.txt"

def count_words(file_name):
    word_count = 0
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

print(count_words(file_name))
