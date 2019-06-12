def frequence(word, letter):
    if word.count(letter) == 1:
        print(word.index(letter))
    elif word.count(letter) < 1:
        print(" ")
    elif word.count(letter) > 1:
        print(word.find(letter), word.find(letter, word.index(letter, word.index(letter)+1, len(word))))

frequence("lenovo", "o")
frequence("bootcamp", "p")
frequence("bootcamp", "w")


        