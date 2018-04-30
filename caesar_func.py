def caesar(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for letter in range(len(sentence)):

        for i in range(len(alphabet)):
            #print("i : " + alphabet[i] + "\nletter = " + sentence[letter])
            #encrypted = ""
            if sentence[letter] not in alphabet:
                result += sentence[letter]
                break

            elif sentence[letter] == alphabet[i]:
                result += alphabet[(i + 13) % 26]
                #result += encrypted
                #print (encrypted)
                break
    
    return result 

#print(caesar(inp))