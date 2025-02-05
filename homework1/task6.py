# TASK 6: File Handling and Metaprogramming 
# objective - read from task6_read_me.txt and count the number of words in the file 

# PART A.
# create lists to hold the names of input files and their corresponding expected outputs 
file_list = ["task6_read_me.txt"]
expected_output_list = [103]

# this function counts the number of words in a given text file 
def count_words(file_name):
    word_count = 0
    # open file for reading
    with open(file_name, 'r') as file:
        # add the number of words in each line to the final word count line by line 
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

# PART B.
# implement metaprogramming techniques to dynamically generate functions 
# for pytest test cases using function names built from the filenames of the text files 

# this function retrieves the base name for a given text file 
def get_base_name(file_name):
    base_name = file_name.rsplit('.', 1)[0]
    return base_name

# this function dynamically creates a test function using metaprogramming techniques 
def create_test_function(target_function, file_name, expected_output):
    
    def generate_test():
        result = target_function(file_name)
        assert result == expected_output

    # assign the test function a name based on the name of the text file 
    test_function_name = f"test_{get_base_name(file_name)}"
    generate_test.__name__ = test_function_name
    print(generate_test.__name__) # for testing
    
    # inject the test function into the global namespace so that it can be recognized by pytest
    globals()[test_function_name] = generate_test

# for every file, create a test function 
for file, expected in zip(file_list, expected_output_list):
        create_test_function(count_words, file, expected)

if __name__ == "__main__":
    # print the number of words for each text file in file_list 
    for file in file_list:
        print(count_words(file))
        