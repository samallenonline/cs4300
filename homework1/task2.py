# TASK 2: Variables and Data Types 

# 1. integers 
def demonstrate_ints():
    # create variable of type int and return to be tested
    int1 = 3 + 5
    
    return int1

# 2. floating-point numbers 
def demonstrate_floats():
    # create variable of type float and return to be tested
    float1 = 2.5 + 2.5

    return float1

# 3. strings 
def demonstrate_strings():
    # create variable of type string and return to be tested
    string1 = "This is a string!"

    return string1

# 4. booleans 
def demonstrate_bools():
    # create variable of type bool and return to be tested 
    value1 = 5
    value2 = 10
    comparison1 = value1 < value2

    return comparison1

if __name__ == "__main__":
    # print the type of value returned from each function 
    print(type(demonstrate_ints()))
    print(type(demonstrate_floats()))
    print(type(demonstrate_strings()))
    print(type(demonstrate_bools()))
