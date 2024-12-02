# def longest_unique_substring(s):
#     start = 0
#     max_length = 0
#     max_substring = ""
#     char_index = {}

#     for i, char in enumerate(s):
#         if char in char_index and char_index[char] >= start:
#             start = char_index[char] + 1

#         char_index[char] = i
#         current_length = i - start + 1

#         if current_length > max_length:
#             max_length = current_length
#             max_substring = s[start:i + 1]

#     return max_substring, max_length


# input_string = input("Enter a string: ")
# substring, length = longest_unique_substring(input_string)
# print(f"The longest substring with unique characters is: '{substring}'")
# print(f"Length of the substring: {length}")





def substrings(str1):
    dict={}
    list=[]
    for word in str1:
        count=0
        tmp=word
        if word not in dict:
                list.append(word)
                for i in str1:
                    if tmp==i:
                      count+=1
                      dict[word]=count
    return list,dict

s="hellol"
s,p=substrings(s)
str="".join(s)
print(f"longest sub string: {str}\n\n{p}")

