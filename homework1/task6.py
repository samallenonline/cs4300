# TASK 6: File Handling and Metaprogramming 

# objective - read from task6_read_me.txt and count the number of words in the file 
# create a list to hold the names of all input files 
file_list = ["task6_read_me.txt"]

def count_words(file_name):
    word_count = 0
    # open file for reading
    with open(file_name, 'r') as file:
        # add the number of words in each line to the final word count line by line 
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

# print the number of words for each text file in file_list 
for file in file_list:
    print(count_words(file))

# implement metaprogramming techniques to dynamically generate function names 
# for pytest test cases based on the filenames of the text files 
