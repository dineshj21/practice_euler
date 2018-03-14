#names_scores.py

import sys
import os
import os.path
import re

def SumOfWords(string):    
    str_list  = [ord(char) - 96 for char in string.lower()]
    total = sum(str_list)
    return total

my_file = "C:\\Users\\d.kumar.jujjuvarapu\\Documents\\p022_names.txt"
for line in open(my_file,"r"):
    lists = line.split(",") 
    
new_list = [re.sub('"','',each) for each in lists]
new_list = sorted(new_list)
result  = 0
for each_word in new_list:
    indexer = new_list.index(each_word)
    indexer += 1
    my_val = SumOfWords(each_word) 
    result += indexer * my_val
    
print(result)    
