import codecs

# Open the file in UTF-16 and read the data
with codecs.open('data.json', 'r', 'utf-16') as file:
    data = file.read()

# Open the file in UTF-8 and write out the data
with codecs.open('data.json', 'w', 'utf-8') as file:
    file.write(data)