#checking if a number passed by the user is a prime number

def is_prime(num):
    check_list = [2,3,4,5,6,7,8,9]
    count = 0
    for i in range(2,len(check_list)):
        if num % i == 0:
            count += 1
    if count > 1:
        return False
    elif count == 1 and num > 20:
        return False
    else:
          return True
        
# for i in range(1, 50):
# 	if is_prime(i + 1):
# 			print(i + 1, end=" ")
# print()
if __name__ == "__main__":
    user_input = int(input("Enter a number to check if it's a prime: "))
    if is_prime(user_input):
        print("{} is a prime number".format(user_input))
    else:
        print("{} is not a prime number".format(user_input))
