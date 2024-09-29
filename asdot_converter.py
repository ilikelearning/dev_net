#!/opt/anaconda3/bin/python

as_multiplier = 65536

#asplain = int(second_2byte) + (int(asdot_split[0]) * as_multiplier)
#asdot = f'{interger}.{int(asplain) - (int(integer) * as_multiplier)}

asdot = input("Enter asdot range | (e.g 65200.5000-65200.6000) :")
#
start_asn = asdot.split("-")[0].strip()
final_asn = asdot.split("-")[1].strip()
final_asn_first_path = int(final_asn.split(".")[0])
df_asn = int(final_asn.split(".")[1]) - int(start_asn.split(".")[1])
start_asn_first_part = int(start_asn.split(".")[0])
start_asn_second_part = int(start_asn.split(".")[1])
start_asn_split = start_asn.split(".")
#


with open ("as_file.txt", "w") as fl:
    for i in range(df_asn+1):
        if start_asn_first_part != final_asn_first_path:
            print(f"ERROR!!!")
            print(f"The first 2BYTE of the asn range must be the same!!!")
            print(f"Please provide a valid range e.g 65200.50 - 65200.60")
            break
        else:
            start_asn_split[1] = str(start_asn_second_part + i)
            asdot = ".".join(start_asn_split)
            asplain = (start_asn_second_part + i) + (start_asn_first_part * as_multiplier)
            print("| The asplain repr. of {} is {} |".format(asdot, asplain))
            print("-"*44)
            fl.write(f"| The asplain repr. of {asdot} is {asplain} |\n")
            fl.write(f"'--------------------------------------------\n")