#!/opt/anaconda3/bin/python3

import sys

as_multiplier = 65536

#asplain = int(second_2byte) + (int(asdot_split[0]) * as_multiplier)

asdot = input("Enter asdot range | (e.g 65200.5000-65200.6000) :")
asdot_list = asdot.split("-")

#check for a valid asdot range. A second asdot must be provided for a valid range

if len(asdot_list) == 1 or len(asdot_list) > 2 or asdot.count(".") != 2:
    print("Please provide a valid asdot range!")
    sys.exit()

start_asn = asdot.split("-")[0].strip()
final_asn = asdot.split("-")[1].strip()
final_asn_first_path = int(final_asn.split(".")[0])
df_asn = int(final_asn.split(".")[1]) - int(start_asn.split(".")[1])
start_asn_first_part = int(start_asn.split(".")[0])
start_asn_second_part = int(start_asn.split(".")[1])
start_asn_split = start_asn.split(".")

with open ("sample_output.txt", "w") as fl:
    for i in range(df_asn+1):
        if start_asn_first_part != final_asn_first_path:
            print(f"ERROR!!!")
            print(f"The first 2BYTE of the first and second asdot notation must be the same!!!")
            print(f"Please provide a valid range e.g 65200.50 - 65200.60")
            break
        else:
            start_asn_split[1] = str(start_asn_second_part + i)
            asdot = ".".join(start_asn_split)
            asplain = (start_asn_second_part + i) + (start_asn_first_part * as_multiplier)
            print("| The asplain repr. of {} is {} |".format(asdot, asplain))
            fl.write(f"| The asplain repr. of {asdot} is {asplain} |\n")
