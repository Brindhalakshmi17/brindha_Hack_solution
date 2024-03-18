'''Find Digits
An integer d is a divisor of an integer n if the remainder of n%d=0 .

Given an integer, 
for each digit that makes up the integer determine whether it is a divisor. 
Count the number of divisors occurring within the integer'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    count=0
    d=list(map(int, str(n)))
    for i in range(len(d)):
        if d[i]>0:
            if n %d[i]==0:
                count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
