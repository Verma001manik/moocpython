import re 
def is_dotw(my_string: str):
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    else :

        return False
def all_vowels(my_string: str) :
    if re.search(r'^[aeiouAEIOU]+$', my_string):
        return True
    else:
        return False
    
def time_of_day(my_string: str):
    if re.search("")
print(all_vowels("eioueioieoieou"))
print(all_vowels("autoooo"))