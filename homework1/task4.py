# TASK 4: Functions and Duck Typing 

# write a function that calculates the final price of a product after applying a given discount percentage 
def calculate_discount(price, discount):
    # calculate discount amount
    discount_decimal = discount / 100
    # calculate final discounted price and return value
    price = price - (price * discount_decimal) 
    return round(price, 2)

if __name__ == "__main__":
    # print the results of the function using various inputs
    print(calculate_discount(50.49, 25))
    print(calculate_discount(50, 25.50))
    print(calculate_discount(50, 25))
    print(calculate_discount(19.99, 15.50))