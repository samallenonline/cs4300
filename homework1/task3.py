# TASK 3: Control Structures 

# implement if statement to check if a number is postive, negative, or zero 
def positive_or_negative(number):
    if number == 0:
        return "Zero"
    elif number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"

# implement for loop to print the first 10 prime numbers 
def first_10_prime():
# intialize variables 
    i = 0
    count = 0
    num = 0
    prime_list = []

    # while loop to ensure only 10 prime numbers are considered
    while count != 10:
        is_prime = True
        # prime numbers must be greater than 1 
        if num < 1:
            is_prime = False

        # check if the number has any factors apart from 1 and itself 
        for i in range(2, num):
            # if so, the number is not prime 
            if (num % i == 0):
                is_prime = False
        
        # if the number is prime, add to list and increment counter
        if is_prime == True: 
                prime_list.append(num)
                count += 1

        # move on to next number 
        num += 1
    return prime_list
        

# implement while loop to find the sum of all numbers from 1 to 100
def sum_of_numbers():
    j = 0
    sum = 0
    while j <= 100:
        sum += j
        j += 1
    
    return sum
    