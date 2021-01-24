import re
import os

print("Hello! Before proceeding, please ensure that the text file is in the same directory as this program.")
print("The program will repeatedly ask you for the file (i.e., sampleText) until the input is one that is \npresent in the directory.")

file_name = input("Text File:")
if file_name not in os.listdir():
    while file_name not in os.listdir():
        print("The text file is not in the directory. Please try again:")
        file_name = input("Text File:")

print("Thank you for the text file.")
print("When you are finished, please input \"end the program\" as a command to terminate the program.")
print("Note that there can only be one space between the \"anagrams\" command and the word, \nas is the case with \"count\". Otherwise, it is not a valid command.")

open_file = open(file_name)
text_unstructured = ""
for i in open_file:
    text_unstructured+=i
open_file.close()

def preprocess(text_unstructured = text_unstructured):
    text_unstructured = re.sub("\s+", " ", text_unstructured)
    text = ""
    pattern = "[A-Za-z]"
    for i in text_unstructured:
        if re.match(pattern, i) or i == " ":
            text+=i.lower()
    text = text.strip()
    return text

text = preprocess()

def non_unique_anagrams(word, text = text): 
    chars_of_word = sorted(list(word))
    list_of_lists_text = []
    
    for i in text.split():
        list_of_lists_text.append(list(i))
        
    prelim_result = ""
    for i in list_of_lists_text:
        if chars_of_word == sorted(i):
            prelim_result+=" " + "".join(i)
    return prelim_result[1:] 

def unique_anagrams(word):
    unique_results = set(non_unique_anagrams(word).split(" "))
    result = ""
    for i in unique_results:
        if len(i) > 0:
            result+=" " + i
    return result[1:] 

def count(word):
    anagrams = non_unique_anagrams(word)
    if len(anagrams) == 0:
        return 0
    else:
        return len(anagrams.split(" "))

def all_anagrams(text = text):
    prelim_result = []
    for i in text.split(" "):
        prelim_result.append(unique_anagrams(i))
    
    intermediary_result = []
    for i in prelim_result:
        if " " in i:
            intermediary_result.append(i)
            
    result = []
    for i in set(intermediary_result):
        result.append(i)
    return result

def top_anagram(text = text):
    anagrams = all_anagrams()
    num_of_spaces = []
    
    for i in anagrams:
        num_of_spaces.append(len(re.findall("\s", i)))
    return anagrams[num_of_spaces.index(max(num_of_spaces))]

stopping_condition = 0
while stopping_condition == 0:
    Command = input("Command:")
    if Command != "end the program":
        if Command == "top anagram":
            print(top_anagram())
        elif Command == "all anagrams":
            for i in all_anagrams():
                print(i)
        elif re.match("anagrams\s[A-Za-z]+$", Command):
            word = re.sub("anagrams\s", "", Command)
            print(unique_anagrams(word))
        elif re.match("count\s[A-Za-z]+$", Command):
            word = re.sub("count\s", "", Command)
            print(count(word))
        else:
            print("The command is not valid. Please try again.")
        print(" ")
    else:
        stopping_condition-=1
        print("You have ended the program.")