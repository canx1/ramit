# Remove "is, in, to, no from given text

text = ["Life is beautiful", "No need to overthink", "Meditation help in overcoming depression"]
newtext=[]

for query in text:
    stopwords = ['is','in','to','no']
    querywords = query.split()
    
    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    newtext.append(result)

print(newtext)