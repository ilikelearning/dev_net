

def PrimeNo(x):
    mylist = []
    div_list = []
    prime_no_check = []
    prime_no_list = []
    for i in range(int(x)+1):
        mylist.append(i)

    for div in mylist:
        if div == 0 or div == 1:
            continue
        div_list.append(div)
    
    for num in mylist:
        for denum in div_list:
            if num % denum == 0 and num != 0:
                prime_no_check.append(num)

    with open("prime_in_a_seq_output_sample.txt", "w") as f:
        for check in prime_no_check:
            if prime_no_check.count(check) == 1:
                prime_no_list.append(check)
        print("Your number Sequence is: {}".format(mylist))
        f.write("Your number Sequence is: {}\n".format(mylist))
        print(f"Prime Numbers in the sequence: {prime_no_list}")
        f.write(f"Prime Numbers in the sequence: {prime_no_list}")
    # print(f"Divisor list is {div_list}")


if __name__ == "__main__":
    print("="*65)
    print("USER INFORMATION:")
    print("A sequence will be created from 0 to your max value.")
    print("The script will then determine all prime numbers in the sequence")
    print("="*65)
    range_val = input("Please provide your max range value: ")
    PrimeNo(range_val)


