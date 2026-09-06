promo_msg="use dharshini15 for 100% offer in ur first order"
if "dharshini15" in promo_msg:
    print("offer applied")

#inorder to find a particular position of a word
feedback= "the driver was kind and polite throughout the ride"
print("position of the word is:", feedback.find("polite"))

#to find the initial with the delimiter "space"
name="dharshini ayyappan"
initials= ([word[0].upper() for word in name.split()])
print(initials)

#for getting the letters out of the list
name="dharshini ayyappan"
initials= "".join([word[0].upper() for word in name.split()])
print(initials)

#cleaning extra spaces
dirty_input= "   airport"
cleaned=dirty_input.strip()
print(cleaned)

#count the number of words
word1="the trip was amazing and the car was clean"
word_count=len(word1.split()) #if u r not using split u will get the number of characters
print(word_count)
