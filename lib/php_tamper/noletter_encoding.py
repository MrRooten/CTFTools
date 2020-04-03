import string
import re
punctuation = string.punctuation

def get_no_letter_list(regex=None):
    res = dict()
    if regex==None:
        regex = r'.'

    new_punctuation = ""
    for i in punctuation:
        if re.match(regex,i):
            new_punctuation += i

    alpha = string.ascii_letters

    for i in alpha:
        for j in new_punctuation:
            for k in new_punctuation:
                if ord(i) == ord(j) ^ ord(k):
                    res[i] = [j,k]

    return res
