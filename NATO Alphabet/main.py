##TODO TURN CHART (DF) INTO A DICT

import pandas

natodata = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")  # find out format type; then make readable

#newdict = {key:value for (index, row) in df.iterrows()
natodict = {row.letter: row.code for (index, row) in natodata.iterrows()}
#print(natodict)

##TODO CREATE A CODE WHERE USER WILL GET A WORD FOR NATO ALPHABET ENTERED ; USE EXCEPTIONS FROM DAY 30
# to allow constant inputs after entry, use this method or create a function to call the process again (DAY 30, 276.)
on = True
while on:
    try:
        user = input("Enter a letter: ").upper()
        output = [natodict[letter] for letter in user]
        answer = "".join(output)  # turned word which is a list into a string
        print(answer)
    except KeyError:
        print("Sorry only letters in the alphabet please.")

# ALT WITHOUT EXCEPTION; ALLOWS ONE WORD ENTRY AT A TIME
# on = True
# while on:
#     user = input("Enter a letter: ").title()
#     for (key, value) in natodict.items():
#         if user == key:
#             print(value)
#     if user == "Stop":
#         on = False
#         print("Off")