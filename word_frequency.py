# def word_fre(word):
#     for w in word:
#         count=0
#         if w !=" ":
#             tmp=w
#         for letter in word:
#             if tmp==letter:
#                 count=count+1
#         print(f"letter {tmp} has repeated {count} times")
# word="hello world"
# word_fre(word)


def word_fre(words):
    dict={}
    for word in words:
        dict[word]=dict.get(word,0)+1
    return dict
word="hello"
frequency=word_fre(word)
for word,count in frequency.items():
    print(f"{repr(word)} : {count}")