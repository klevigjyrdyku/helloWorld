message = input(">")
words = message.split(' ')
emojis = {
    ":)": "8",
    ":(": "7"
}
outpute = ""
for word in words:
    outpute  += emojis.get(word, word ) + " "
print(outpute)