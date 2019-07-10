#Patricia Shatz
#Module 8 Assignment 
#Created on Sun May 5 13:24:00 2019
#Modified on Mon May 6 03:32:00 2019 

#data is the text inputted by the user and key represents the shift that should occur with 
#each character of the user's original message


def cipher(dataText, key):
    cipherString = ''
    for char_data in dataText:
        #shift the number according to the key and wrap it every 26 numbers
        cipherVals = (ord(char_data) + key % 26)
        shiftLetter = chr(cipherVals)
        cipherString += shiftLetter
    #returns ciphered string without any whitespaces
    return cipherString
       
def decipher(cipherString, key):
    decipherString =''
    for char_data in cipherString:
        #shift the number according to the key and wrap it every 26 numbers
        cipherVals = (ord(char_data) - key % 26)
        shiftLetter = chr(cipherVals)
        decipherString += shiftLetter
    #returns deciphered string without any whitespaces    
    return decipherString               
 
def main(): 
    inputStr = str(input('Enter a string to be ciphered: '))
    shiftNum = int(input('Enter an integer that will be your key to shift your values: '))
    #remove any whitespaces from strings so that they are not also ciphered and deciphered
    inputStr = inputStr.replace(" ","")
    cipherText = cipher(inputStr,shiftNum)
    print('Your ciphered string is: ', cipherText)
    decipherText = decipher(cipherText, shiftNum)
    print('Your deciphered string is: ', decipherText)


main()

 