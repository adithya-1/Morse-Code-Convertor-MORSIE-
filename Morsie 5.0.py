import sys
import winsound
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
          'C':'-.-.', 'D':'-..', 'E':'.', 
          'F':'..-.', 'G':'--.', 'H':'....', 
          'I':'..', 'J':'.---', 'K':'-.-', 
          'L':'.-..', 'M':'--', 'N':'-.', 
          'O':'---', 'P':'.--.', 'Q':'--.-', 
          'R':'.-.', 'S':'...', 'T':'-', 
          'U':'..-', 'V':'...-', 'W':'.--',
          'X' : '-..-', 'Y' : '-.--', 'Z' : '--..', 
           '1':'.----', '2':'..---', '3':'...--', 
          '4':'....-', '5':'.....', '6':'-....', 
          '7':'--...', '8':'---..', '9':'----.', 
          '0':'-----', ',':'--..--', '.':'.-.-.-', 
          '?':'..--..', '/':'-..-.', '-':'-....-', 
          '(':'-.--.', ')':'-.--.-',' ':' '}


def encrypt():
        w=[]
        n=input("Enter a sentence : ")
        a=n.split()
        for i in a:
                c=i.upper()
                b=list(c)
                q =[]
                for j in b:
                        if j in MORSE_CODE_DICT:
                                q.append(MORSE_CODE_DICT[j])
                        else:
                                print("Invalid statement.Please enter valid statement") 
                                winsound.PlaySound("Nan-IS.wav",winsound.SND_FILENAME)
                                sys.exit()
                e = "".join(q)
                w.append(e + " ")
                r="".join(w)
        print("The morse of the given sentence '" + n +"' is", r)
        i=1
        while i!=0:
                n=input("Do u wish to hear the audio\n1.Yes\n2.No\n")
                if n=='1':
                        for i in r.split():
                                i=list(i)
                                for j in i:
                                        if j=='.':
                                                winsound.PlaySound("dot.wav",winsound.SND_FILENAME)
                                        else:
                                                winsound.PlaySound("dash.wav",winsound.SND_FILENAME)
                        break
                elif n=='2':
                        break
                else:
                        print("Invalid choice\nPlease enter valid choice")
                i+=1
        
                    
        
def decrypt():
    a=[]
    b=[]
    i=1
    while i!=0:
        n=input("Enter each word of the code by giving space after each letter:")
        if n=='exit':
            break
        else:
            c=[]
            y=n.split()
            for i in y:
                for key,value in MORSE_CODE_DICT.items():
                    if i==value:
                        c.append(key)
            a.append("".join(c))
        for j in n.split():
            if j not in MORSE_CODE_DICT.values():
                print("Invalid code.Please enter valid code")
                winsound.PlaySound("Nan-IC.wav",winsound.SND_FILENAME)
                break
    
            
    for i in a:
        b.append(i.lower())
    b=' '.join(b)
    print("The converted Morse Code is",b)
    i=+1

i=1
while i!=0:
        if i==1:
                winsound.PlaySound("Nan-intro.wav",winsound.SND_FILENAME)
        else:
                winsound.PlaySound("Nan-Ask.wav",winsound.SND_FILENAME)
        n=input("Please choose one of the following options\n1.Convert text to morse\n2.Convert morse to text\n3.Exit\nEnter 1,2 or 3:")
        if n=='1':
                print("You have chosen to convert text to morse code")
                winsound.PlaySound("Nan-TM.wav",winsound.SND_FILENAME)
                encrypt()
        elif n=='2':
                print("You have chosen to convert morse to text")
                winsound.PlaySound("Nan-MT.wav",winsound.SND_FILENAME)
                decrypt()
        elif n=='3':
                winsound.PlaySound("Nan-Thanks.wav",winsound.SND_FILENAME)
                sys.exit()
        else:
                print('Invalid Choice')
        i+=1


