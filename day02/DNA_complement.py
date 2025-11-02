DNA_original = input("Enter your sequence: ")
DNA_complement = ""

for base in DNA_original:
    if base == "A":
        DNA_complement += "T"
    elif base == "G":
        DNA_complement += "C"
    elif base == "T":
        DNA_complement += "A"
    elif base == "C":
        DNA_complement += "G"
print(DNA_complement)

