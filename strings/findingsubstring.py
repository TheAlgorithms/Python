#to find no. of substring in given input.
# Sample Input
# ABCDCDC
# CDC
# Sample Output
# 2




def count_substring(string, sub_string):
    count=0
    lenn=len(string)
    index=string.find(sub_string,0,lenn)
    while index!=-1:
        count=count+1
        index=string.find(sub_string,index+1,lenn)
    return count
