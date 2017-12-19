from textblob import TextBlob as tb

text = " "
while text != "":
    text = input("Type the text: ")
    print("The polarity is: %f\n" %(tb(text).sentiment.polarity))
