word = input("Please enter a word: ")
counter = 0
vowels = ['a', 'e', 'i', 'o', 'u']
vcount = 0

while counter < len(word):
    if word[counter] in vowels:
        vcount += 1
    counter += 1

print(vcount)
