def begin_with_vowel(words:list):
    vowel = ["a" , "e", "i", "o", "u"]
    result = [word for word in words if word.lower()[0] in vowel ]
    return result
word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
for vowelled in begin_with_vowel(word_list):
    print(vowelled)