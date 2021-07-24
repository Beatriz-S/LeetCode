
'''
A text file has 456789 letters. 
If the text file is text wrapped to 80 characters per line (a line folds to the next after 80 columns of characters from the left), 
the number of lines with letters in the text file would be: 5710
 . How many letters are in the last line? 69

Hint: It is considered a line regardless you have a full line or a partial line.
'''

import math
result=456789/80
print(math.ceil(result))
remainder=456789%80
print(remainder)