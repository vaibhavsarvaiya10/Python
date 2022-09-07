#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    var1 = list(sentence.split(" "))
    var2 = var1[::-1]
    var3 = " ".join(var2)
    print(var3.swapcase())

if __name__ == '__main__':
    sentence = input()
    
    result = reverse_words_order_and_swap_cases(sentence)
