import re

"""
Write a program that turns a sentence into camel case. The first word is lowercase, the rest of the words have their
initial letter capitalized, and all of the words are joined together. For example, with the input "fOnt proCESSOR and
ParsER", your program will output "fontProcessorAndParser".
Optional extra question: print a warning message if the input will not produce a valid variable name.
You don't need to be exhaustive in checking, but test for a few common issues, such as starting with a number, or
containing invalid characters such as # or + or ".
Test your program with different example inputs, and comment your code.
"""

def camel(sentence):
    try:
        #Strip out special characters https://docs.python.org/3/library/re.html#re.sub
        stripped_sentence = re.compile('[^a-zA-Z ]').sub('', sentence)
        #Raise error if invalid input https://docs.python.org/3/tutorial/errors.html
        if len(sentence) != len(stripped_sentence):
            raise ValueError(sentence)
        #Make all characters lowercase and split into a list
        sentence_list = stripped_sentence.lower().split(" ")
        #https://www.geeksforgeeks.org/string-capitalize-python/
        #https://www.geeksforgeeks.org/python-map-function/
        #https://www.programiz.com/python-programming/methods/list/index
        return "".join(map(lambda x: x.capitalize() if sentence_list.index(x) > 0 else x, sentence_list))
    except ValueError as err:
        return f"{type(err)}: invalid characters in \"{err}\""

def banner():
    #Displays a banner
    message = """
                          _ _____               ______                                    _ 
                         | /  __ \              | ___ \                                  | |
  ___ __ _ _ __ ___   ___| | /  \/ __ _ ___  ___| |_/ / __ ___   __ _ _ __ __ _ _ __ ___ | |
 / __/ _` | '_ ` _ \ / _ \ | |    / _` / __|/ _ \  __/ '__/ _ \ / _` | '__/ _` | '_ ` _ \| |
| (_| (_| | | | | | |  __/ | \__/\ (_| \__ \  __/ |  | | | (_) | (_| | | | (_| | | | | | |_|
 \___\__,_|_| |_| |_|\___|_|\____/\__,_|___/\___\_|  |_|  \___/ \__, |_|  \__,_|_| |_| |_(_)
                                                                 __/ |                      
                                                                |___/  
    """
    return message

def instructions():
    #Displays instructions
    instructions = "Enter a sentence to convert it to camelCase. Do NOT enter any special characters."
    return instructions

if __name__ == "__main__":
    print(banner())
    print(instructions())
    #User enters a sentence
    sentence = input("Please enter a sentence:\n").strip()
    print(camel(sentence))
