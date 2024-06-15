#4th December 2021
def split_s(string):
    split = []
    empty = ''
    for words in string:
        if words == ' ':#have space
            split.append(empty)#append blank space in split(list)
            empty = ''
            
        else:
            empty+=words#else add the rest of the words in this string
    if True:
        split.append(empty)
    return split
print(split_s('Split me y'))
