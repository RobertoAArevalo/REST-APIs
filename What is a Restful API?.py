#API

def raise_to_power(base_num, pow_num): #This is a function with 2 inputs. base number and pow number.
    result = 1 #it will result the math
    for index in range(pow_num): #it will loop through this for loop as many times as is specified in pow_num
        result = result * base_num #multiplies the result by base_num
    return result # calls the result to be returned

print(raise_to_power(3, 4))