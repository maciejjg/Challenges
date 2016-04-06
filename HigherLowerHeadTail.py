# Higher/Lower Heads/Tail

sentence = 'tHis IS my oPinioN'


# first solution 
def foo(x):
    new_sentence = x.lower()
    new_sentence = " ".join(word[0].upper() + word[1:] for word in new_sentence.split())
    return new_sentence
print(foo(sentence))

# second solution
# print(sentence.title())
