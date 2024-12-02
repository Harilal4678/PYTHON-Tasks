def read_strings(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    if sorted(str1)==sorted(str2):
        return f"{str1} and {str2} are anagarams"
    else:
        return f"not anagrams"
    
s1="hello "
s2="lleho"
answer=read_strings(s1,s2)
print(answer)