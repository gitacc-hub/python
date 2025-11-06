#message="I am the first text\n I am the second text\nI am the third text"
with open("text.txt","a",encoding="utf-8")as file:
    file.write("\nThis is the appended line.")
with open("text.txt","r") as file:
    print(file.read())