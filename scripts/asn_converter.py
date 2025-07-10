

#!/opt/anaconda3/bin/python3

as_multiplier = 65536

#asdot = f'{interger}.{int(asplain) - (int(integer) * as_multiplier)}
#asplain = int(remainder) + (int(integer) * as_multiplier)

print()
asn = input("Enter asn value in asdot or asplain notation :")

if asn.count(".") == 0:
    asplain_integer = int(asn) // as_multiplier
    asplain_remainder = int(asn) - (asplain_integer * as_multiplier)
    print("-"*41)
    print("The asdot for {} is {}.{}".format(asn, asplain_integer, asplain_remainder))
    print("-"*41)
elif asn.count(".") != 0 and asn.count(".") > 1:
    print("ERROR!!!!")
    print("Please provide a valid asdot notation!")
else:
    asdot_integer = int((asn.split(".")[0]).strip())
    asdot_remainder = int((asn.split(".")[1]).strip())
    asplain = asdot_remainder + (asdot_integer * as_multiplier)
    print("-"*43)
    print(f"The asplain for {asn} is {asplain}")
    print("-"*43)

