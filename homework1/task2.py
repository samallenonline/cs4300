# TASK 2: Variables and Data Types 

# 1. integers 
def demonstrate_ints():
    # perform various calculations using ints and return the results 
    int1 = 1 + 3
    int2 = 5 - 5
    int3 = 3 * 7
    
    return int1, int2, int3

# 2. floating-point numbers 
def demonstrate_floats():
    # perform various calculations using floats and return the results 
    float1 = 2.5 + 2.5
    float2 = 1.3 - 0.3
    float3 = 3.5 * 7.2

    return float1, float2, float3

# 3. strings 
def demonstrate_strings():
    # perform various operations using strings and return the results 
    string = "Hi there"
    uppercase_string = string.upper()
    first_letter = string[0]

    return string, uppercase_string, first_letter

# 4. booleans 
def demonstrate_bools():
    # perform various logical operations using bools and return the results 
    value1 = 5
    value2 = 10
    value3 = 5
    comparison1 = value1 < value2
    comparison2 = value1 > value2
    comparison3 = value1 == value3

    return comparison1, comparison2, comparison3

if __name__ == "__main__":
    # print the results of each function to demonstrate the use of each data type 
    print(demonstrate_ints())
    print(demonstrate_floats())
    print(demonstrate_strings())
    print(demonstrate_bools())
