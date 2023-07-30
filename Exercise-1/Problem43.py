
# Python Program to Count the Number of Each Vowel

vowels='aeiou'

str='Hello, have you tried our tutorial section yet?'

str=str.casefold()

count={}.fromkeys(vowels,0)

for char in str:
    if char in count:
        count[char]+=1

print(count)


