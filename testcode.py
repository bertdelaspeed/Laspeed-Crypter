import webbrowser
from tkinter import *

from PIL import ImageTk, Image

def fonc(event):
    url='commentcamarche.net'
    webbrowser.open_new(url)
root = Tk()
img = ImageTk.PhotoImage(Image.open("PayPalButton.png"))
panel = Label(root, image = img)
panel.bind("<Button-1>",fonc)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()

cipher = ""
i = 0
j = 0

# As it is a text box we need to specify the beginning and ending of the get()
text = input("1")

key = input("2")

# key=getpass.getpass(prompt='Key \n')

# Getting the length of the plain text
text_length = len(text)

# Getting the length of the encryption key
key_length = len(key)
print(key_length)



# Till we reach the end of the plain text
while (i != text_length):


    # In case we're at the end of the encryption key, go back to it's starting point
    if j == key_length:
        j = 0

    # print(b)

    # In this part we make sure that the character inputed is lowchar

    p = 0
    print("Special cases")
    while (p < 255):
        if(not chr(p).isdigit() and not chr(p).isalpha()):
            print(p)
        p += 1



    if (ord(text[i]) >= ord('a')) and (ord(text[i])) <= ord('z'):
        if (key[j].isdigit()):
            a=int(key[j])
            print(key[j])
            print(ord(text[i]))
            if ((ord(text[i])) + a) > 122:
                modulo = ((ord(text[i]) + a) % 122)
                while (modulo > 122 or modulo<96):
                    modulo = (modulo % 122) + 96

                cipher += chr(modulo)



        else:
            b = ord(key[j]) - ord('a')
            # A lil twist here is that i'm using 96 instead of 97 so you could still fail the decryption as i'm at -1 char
            # a=97 and z=122, so in case by adding the encryption number to the element of the text
            # we pass 122, pull it back into the range [97-122]
            if (ord(text[i]) + b) > 122:

                # In some cases checking only once results in having a number greater than 122 so
                # I made a loop to make sure that we stay in the range and +96 to start from a
                modulo = ((ord(text[i]) + b) % 122) + 96
                while (modulo > 122):
                    modulo = (modulo % 122) + 96

                cipher += chr(modulo)
                print("In small letter :", cipher)
                # By just doing modulo 122 we'll go back to 1,2,3 etc but ne need to be at least at 97 which is a so we add 96 on top of it
                # cipher += chr(((ord(text[i])+b)%122)+96)
            else:
                cipher += chr((ord(text[i]) + b))



                # In this part we make sure that the character inputed is Upperchar

        if (ord(text[i]) <= 31):
            cipher += chr(ord(text[i]))

        if (ord(text[i]) >= ord('A')) and (ord(text[i])) <= ord('Z'):

            b = ord(key[j]) - ord('A')
            # A=65 and Z=90, so in case by adding the encryption number to the element of the text
            # we pass 90, pull it back into the range [65-90]
            if (ord(text[i]) + b) > 90:

                modulo = ((ord(text[i]) + b) % 90) + 64
                # In some cases checking only once results in having a number greater than 90 so
                # I made a loop to make sure that we stay in the range and +64 to start from A
                while (modulo > 90):
                    modulo = (modulo % 90) + 64
                cipher += chr(modulo)


                # By just doing modulo 90 we'll go back to 1,2,3 etc but ne need to be at least at 97 which is a so we add 96 on top of it
                # cipher += chr(((ord(text[i]) + b) % 90) + 64)

            else:
                cipher += chr((ord(text[i]) + b))
                # print(cipher)
            print("In Big letter :", cipher)
        # Now taking care of character from space to @ but i'm not taking care of @ as its value is 64 and there's a possiblity that Uppercase%90=0+64
        # Hence not taking care of @ -> 64
        if (ord(text[i]) >= 32 and (ord(text[i]) < 64)):
            cipher += chr(ord(text[i]) + 1)

        if (ord(text[i]) >= 91 and (ord(text[i]) <= 96)):
            cipher += chr(ord(text[i]))
        print("In special :", cipher)

        # Now taking care of characters from { which is 123 to ~ which is 126
        if (ord(text[i]) >= 123 and (ord(text[i]) < 127)):
            # We need to be careful on this one as 127 = Del so
            # if(ord(text[i])==126):
            #     cipher +="DEL"
            # else:
            #     cipher += chr(ord(text[i]) + 1)
            cipher += chr(ord(text[i]))
            print("In Last specials :", cipher)
            # ACTUALLY NO I'LL JUST LEAVE IT AS IT IS


            # else:
            #     cipher += chr(ord(text[i]))
            #     print("In else case :", cipher)

    i += 1
    j += 1

print(cipher)
