#C1840336.
#The programme generates the proper outcome as expected.

#! /usr/bin/python3
import re

##CMT115 COURSEWORK 2018/19 ###
###############################
##You need to implet the following methods:
##
##Question 1
##anagram_validator()  [15 marks]
##
##Question 2
##credit_card_validator()  [15 marks]

################################

###################################################
# Question 1: Check for anagrams:#
###################################################
def read_anagram(file_name):
    #Input: a file name.
    f = open(file_name, "r+")
    with open(file_name, "r+") as f:
        #Split lines.
        #Code adapted from stackoverflow.
        #Accessed 02/12/18.
        #https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
        x = [line.split() for line in f]
        #End of reference.
        
        #Split numbers into separate numbers.
        y = [i[0].split(',') for i in x]
        #Return: a nested list of two words list.    
        return y
read_anagram("anagram.txt")

pass

def anagram_validator(anagram):
    #Input from the output of "read_anagram()".
    input = read_anagram("anagram.txt")
    lst = [item[0] for item in input]
    lst2 = [item[1] for item in input]
    #Return: list of "anagrams" or "Not anagrams".
    anagram = []
    for f,s in zip(lst,lst2):
        if set(f) == set(s):
            anagram.append("Anagrams")
        else:
            anagram.append("Not anagrams")
    print(anagram)
    return anagram
    for i in anagram:
        print(i)
############################################
# Question 2: Validate credit cards         #
############################################
def read_credit_cards(file_name):
    #Input: a file name.
    f = open(file_name, "r+")
    #Return tuple of numbers.
    for line in f:
        line = line.split(',')
        tup = tuple(line)
        return tup
read_credit_cards("credit_cards.txt")

pass

def credit_card_validator(numbers):
    #Regular expression for credit cards.
    #Adapted from codereview stackexchange.
    #Accessed 02/12/18.
    #https://codereview.stackexchange.com/questions/169530/validating-credit-card-numbers
    pattern = r'^(?![-\d]*([0-9])(?:-?\1){3,})[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$'
    #End of reference.

    #Input: tuple of numbers.
    input = read_credit_cards("credit_cards.txt")

    validation = []

    #Match credit card numbers and validation.
    #Code for re.match based on page from guru99.
    #Accessed 02/12/18.
    #https://www.guru99.com/python-regular-expressions-complete-tutorial.html
    for credit_card_numbers in input:
        if re.match(pattern, str(credit_card_numbers)):
            validation.append("{}:Valid".format(str(credit_card_numbers)))
        else:
            validation.append("{}:Invalid".format(str(credit_card_numbers)))
    #End of reference.

    #Return: dictionary of credit card numbers where key is the number and value if valid or invalid.
    #Code for dictionary adapted from python for beginners.
    #Accessed 02/12/18.
    #https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python 
    dict_credit_cards = {}
    
    for credit_cards in validation:
        item = credit_cards.split(':')
        dict_credit_cards[item[0]] = item[1]
    print(dict_credit_cards)
    return dict_credit_cards
    #End of reference.
pass

def print_credit_card_summary(dict_o):
    #Input: dict.
    input = credit_card_validator("numbers")
    #Return: printing summary of validation result - space between credit card and status is 40 width.
    #Code to print summary adapated from stackoverflow.
    #Accessed 02/12/18.
    #https://stackoverflow.com/questions/33042391/how-to-print-dictionary-keys-and-values-in-python
    print("\n".join("{:<40s}\t{}".format(k, v) for k, v in input.items()))
    #End of reference.
####### THE CODE BELOW IS FOR TESTING###################
############### DO NOT  CHANGE #########################

import sys

if __name__ == '__main__':
    # Take care of the console inputs
    if len(sys.argv) <= 1:
        sys.argv = ['', "anagram.txt", "credit_cards.txt"]
    stars = '*' * 40
    print(stars)
    print("Testing Question 1 --- Anagrams?")
    print(stars)

    # testing reading_anagrams
    try:
        anagram = read_anagram(sys.argv[1])
        if not anagram:
            print("read_anagram() returns None.")
        else:
            print("anagram: ", anagram)
            print()
    except Exception as e:
        print("Error (readnumbers()): ", e)

    # testing anagram_validator
    Anagrams = 0
    NAnagrams = 0
    try:
        if not anagram:  # Question 1 has not been implemented
            print("anagram_validator() skipped....")
        else:
            result = anagram_validator(anagram)
            if result == None:
                print("anagram_validator() returns None.")
            else:
                for i in result:
                    if i == "Anagrams":
                        Anagrams += 1
                    elif i == "Not anagrams":
                        NAnagrams += 1
                print("Number of valid Anagrams is {} and Not anagrams is {}.".format(Anagrams, NAnagrams))

    except Exception as e:
        print("Error (anagram_validator()):", e)

    # testing  Question 2
    print("\n\n" + stars)
    print("Testing Question 2 --- Credit Card Validator")
    print(stars)

    # Testing reading_credit_cards
    try:
        tup = read_credit_cards(sys.argv[2])
        if not tup:
            print("read_credit_cards() returns None.")
        else:
            print("The tuple of credit_cards: {}".format(tup))
    except Exception as e:
        print("Error (read_credit_cards()):", e)

    # Testing credit_card_validator
    vcc = 0
    ivcc = 0
    try:
        if not tup:  # Readin_Question 2 has not been implemented
            print("credit_card_validator() skipped...")
        else:
            cc_dict = credit_card_validator(tup)
            tmp_cc_dict = cc_dict
            if not cc_dict:
                print("credit_card_validator()  returns None.")
            else:
                for items in cc_dict.keys():
                    if cc_dict[items] == "Valid":
                        vcc += 1
                    elif cc_dict[items] == "Invalid":
                        ivcc += 1
                print("Number of valid credit cards is {} and invalid {}.".format(vcc, ivcc))
    except Exception as e:
        print("Error (credit_card_validator()):", e)

    # testing  Question 2
    print("\n\n" + stars)
    print("Testing Question 2b --- Print Credit Card Summary")
    print(stars)
    # Testing print_credit_card_summary
    try:
        if not tmp_cc_dict:  # Dict credit card output has not been implemented
            print("print_credit_card_summary() skipped...")
        else:
            import io  # do not delete this line
            from contextlib import redirect_stdout  # do not delete this line

            f = io.StringIO()
            with redirect_stdout(f):
                print_credit_card_summary(tmp_cc_dict)
                out = f.getvalue()
            if not out:
                print("print_credit_card_summary()  returns None.")
            else:
                count44 = 0
                count46 = 0
                for line in out.splitlines():
                    if len(line) - len(line.split()) == 44:
                        count44 += 1
                    elif len(line) - len(line.split()) == 46:
                        count46 += 1
                if count44 == vcc and count46 == ivcc:
                    print("Your format looks good")
                else:
                    print("You might have some issues in your summary format")

    except Exception as e:
        print("Error (print_credit_card_summary()):", e)