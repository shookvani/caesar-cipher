#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function    T N E Y I O 

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26 # this is index of that letter in the string 
            secret = secret + alpha[spot] # encrypting that specific letter and adding it to the thing 
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

def decode(message, key):
    #We will want to decode the message here.
    #FOR ALL KEYS
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''

    for k in range(len(message)):
        ind=(LETTERS.index(message[k])-key)%len(LETTERS)
        translated=translated+LETTERS[ind]



    '''
    for key in range(len(LETTERS)):
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
    '''
    return translated
    #print('Key Shift #%s: %s' % (key, translated))

def main(message,key):
    #message = input("Enter a message: ")
    #key = int(input("Enter a key: "))

    secret = encode(message, key)
    print ("Encrypted:", secret)
    x = decode(secret, key)
    print ("Decrypted:", x)


main("hello",7)
