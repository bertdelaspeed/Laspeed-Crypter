import webbrowser
from tkinter import *

import pyperclip
from PIL import ImageTk,Image


#emo = (emoji.emojize(" :sunglasses:", use_aliases=True))


def payp(event):

    url='https://www.linkedin.com/in/wilfried-bertrand-wetta-946507149/'

    webbrowser.get(using='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new(url) or webbrowser.open(url)

def faceb(event):
    url='https://www.facebook.com/bert.lateuf.3'
    webbrowser.get(using='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open_new(url) or webbrowser.open(url)



decoded = ""

def Decrypter():

    global decoded
    decoded = ""
    i = 0
    j = 0

    # As it is a text box we need to specify the beginning and ending of the get()
    text = texto.get("1.0", "end-1c")

    key = code.get()

    length = len(text)
    length2 = len(key)

    while (i != length):

        #print("in decrypt")

        if j == length2:
            j = 0

# Key seems to be more important here so, we gotta check witht he key first
            #For example by checking with the text first, when we encrypt G with @ it gives ( or ) but this is considered by the >32 - <64 if so
            #we use the key as 1st checker
        if (key[j].isdigit()):
            #print("in digit ?")
            if (ord(text[i]) >= ord('a')) and (ord(text[i])) <= ord('z'):

                a = int(key[j])
                #print(key[j])
                #print(ord(text[i]))
                if ((ord(text[i])) - a) < 97:
                    modulo = ((ord(text[i]) - a)+26)
                    # while (modulo > 122 or modulo < 96):
                    #     modulo = (modulo % 122) + 96

                    decoded += chr(modulo)

                else:
                    decoded += chr(ord(text[i])-a)

            if (ord(text[i]) >= ord('A')) and (ord(text[i])) <= ord('Z'):

                #print("in is digit")
                a = int(key[j])
                #print(key[j])
                #print(ord(text[i]))
                if ((ord(text[i])) - a) < 65:
                    modulo = ((ord(text[i]) - a)+26)
                    # while (modulo > 122 or modulo < 96):
                    #     modulo = (modulo % 122) + 96

                    decoded += chr(modulo)

                else:
                    decoded += chr(ord(text[i])-a)


            elif (ord(text[i]) >= 32 and (ord(text[i]) < 64)):

                decoded += chr(ord(text[i]) - 1)


            elif (chr(ord(text[i])) == "@"):
                decoded += chr(ord(text[i]))

            elif (ord(text[i]) >= 91 and (ord(text[i]) <= 96)):

                decoded += chr(ord(text[i]))

            elif (ord(text[i]) >= 123 and (ord(text[i]) < 127)):

                decoded += chr(ord(text[i]))

        elif (not ((key[j]).isdigit()) and (not ((key[j]).isalpha()))):

            #print("in decrypt not digit and not alpha")

            if ((text[i].isalpha())):

                bert = ord(text[i])+3

                decoded += chr(bert)

            elif (ord(text[i])<=31):

                decoded += chr(ord(text[i]))


            elif (text[i].isdigit()):
                decoded += chr(ord(text[i]))

            elif ((ord(text[i]))>=ord(chr(62))) or ((ord(text[i]))>=ord(chr(94))):
                decoded += chr(ord(text[i])+3)
            else:
                decoded += chr(ord(text[i]))

            # elif(ord(text[i])==32):
            #     decoded += chr(ord(text[i]))
            # elif (ord(text[i]) > 32 and (ord(text[i]) < 64)):
            #
            #     bert = abs((ord(text[i]) + ord(key[j])))
            #     decoded += chr(bert)
            # #     # bert = ((ord(text[i])))
            # #     #
            # #     # if (bert - 33) < 33:
            # #     #
            # #     #     decoded += chr(bert -32 + ord(key[j]))
            # else:# (text[i].isupper()):
            #     bert = ((ord(text[i])))
            #
            #     decoded += chr(bert + ord(key[j]))
            # else:
            #     decoded += chr(ord(text[i]))


        else:
            if (ord(text[i]) >= ord('a')) and (ord(text[i])) <= ord('z'):


                b = ord(key[j]) - ord('a')
                # A lil twist here is that i'm using 96 instead of 97 so you could still fail the decryption as i'm at -1 char
                # a=97 and z=122, so in case by adding the encryption number to the element of the text
                # we pass 122, pull it back into the range [97-122]
                if (ord(text[i]) - b) < 97:

                    # In some cases checking only once results in having a number greater than 122 so
                    # I made a loop to make sure that we stay in the range and +96 to start from a
                    modulo = ((ord(text[i]) - b) + 26)
                    # modulo = ((ord(text[i]) - b) % 97) + 96
                    # while (modulo > 122):
                    #     modulo = (modulo % 122) + 96

                    decoded += chr(modulo)
                    # By just doing modulo 122 we'll go back to 1,2,3 etc but ne need to be at least at 97 which is a so we add 96 on top of it
                    # decoded += chr(((ord(text[i])+b)%122)+96)
                else:
                    decoded += chr((ord(text[i]) - b))

            if (ord(text[i]) >= ord('A')) and (ord(text[i])) <= ord('Z'):


                b = ord(key[j]) - ord('A')
                # A=65 and Z=90, so in case by adding the encryption number to the element of the text
                # we pass 90, pull it back into the range [65-90]
                if (ord(text[i]) - b) < 65:

                    modulo = ((ord(text[i]) - b) + 26)
                    # While testing I found a case where I got values that ain't numbers so, keep adding 26 till we get it
                    while (modulo < 65):
                        modulo += 26

                    # modulo = ((ord(text[i]) + b) % 90) + 64
                    # # In some cases checking only once results in having a number greater than 90 so
                    # # I made a loop to make sure that we stay in the range and +64 to start from A
                    # while (modulo > 90):
                    #     modulo = (modulo % 90) + 64
                    decoded += chr(modulo)


                    # By just doing modulo 90 we'll go back to 1,2,3 etc but ne need to be at least at 97 which is a so we add 96 on top of it
                    # decoded += chr(((ord(text[i]) + b) % 90) + 64)

                else:
                    decoded += chr((ord(text[i]) - b))

            elif (ord(text[i]) >= 91 and (ord(text[i]) <= 96)):

                decoded += chr(ord(text[i]))

            elif (ord(text[i]) >= 123 and (ord(text[i]) < 127)):

                decoded += chr(ord(text[i]))


            elif (ord(text[i]) >= 32 and (ord(text[i]) < 64)):
                decoded += chr(ord(text[i]) - 1)

            elif (chr(ord(text[i])) == "@"):
                decoded += chr(ord(text[i]))

        if(ord(text[i])<=31):
            decoded += chr(ord(text[i]))

            # In this part we make sure that the character inputed is Upperchar



        #if (key[j].isdigit()):



        # if (not ((key[j]).isdigit()) and (not ((key[j]).isalpha()))):
        #
        #     if (ord(text[i]) >= ord('A')) and (ord(text[i])) <= ord('Z'):
        #
        #         #print("\nin isnt alpha and digit decrypt")
        #
        #         bert = ((ord(text[i])))
        #
        #         decoded += chr(bert+ord(key[j]))

                # if the result is less than 32 that means I'd added 32 to make it appear so
                # on the result we retract the 32 added which gives the supposed invisible value on top of which we add the value of the key
                # print(bert)





        #else:




                # Now taking care of character from space to @ but i'm not taking care of @ as its value is 64 and there's a possiblity that Uppercase%90=0+64
                # Hence not taking care of @ -> 64



            # Now taking care of characters from { which is 123 to ~ which is 126
        # if (ord(text[i]) >= 123 and (ord(text[i]) < 127)):
        #     # We need to be careful on this one as 127 = Del so
        #     # if(ord(text[i])==126):
        #     #     decoded +="DEL"
        #     # else:
        #     #     decoded += chr(ord(text[i]) + 1)
        #     decoded += chr(ord(text[i]))
        #     # ACTUALLY NO I'LL JUST LEAVE IT AS IT IS
        #
        # if (ord(text[i]) >= 91 and (ord(text[i]) <= 96)):
        #     decoded += chr(ord(text[i]))

        i += 1
        j += 1

    #print(decoded)

    pyperclip.copy(decoded)
    decoded += "\n\n** SUCCESSFULLY DECRYPTED -> USE CTRL + V <- **"

    # Mescod.delete(0.0,END)

    # Make the text box editable
    Mescod.configure(state='normal')

    Mescod.delete(0.0, END)

    Mescod.insert(END, decoded)
    # Text box not editable
#    Mescod.configure(state='disabled')

    # God ! I suffered on this one ahaha You gotta set decoded back to empty otherwise it keeps everything in it as it's a global variable
#    decoded = ""


cipher = ""

def Crypter():



    global cipher
    cipher = ""
    i=0
    j=0

    #As it is a text box we need to specify the beginning and ending of the get()
    text=texto.get("1.0","end-1c")



    key=code.get()

    #key=getpass.getpass(prompt='Key \n')

    #Getting the length of the plain text
    text_length=len(text)

    #Getting the length of the encryption key
    key_length=len(key)

    #Till we reach the end of the plain text
    while(i!=text_length):
        #In case we're at the end of the encryption key, go back to it's starting point
        if j==key_length:
            j=0

        #print(b)

        #In this part we make sure that the character inputed is lowchar
        if (key[j].isdigit()):
#In case the key is a digit (a case i didn't take care of at the beginning
        #Here we check is it's a digit
            if (ord(text[i]) >= ord('a')) and (ord(text[i])) <= ord('z'):

                a = int(key[j]) #Because there a conversion prob or someth str to int the comparison isn't getting evaluated so we storing the
                #array key element in a variable

                #print(key[j])
                #print(ord(text[i]))

                #if by multiplying the ord of text by the digit, we get a number greater than 122 (z) we modulo it by 122
                if ((ord(text[i])) + a) > 122:
                    modulo = ((ord(text[i]) + a) % 122)
                    #In case we get a result lesser than 96(a) or greater than 122(z) we modulo it and add 96
                    while (modulo > 122 or modulo < 96):
                        modulo = (modulo % 122) + 96

                    cipher += chr(modulo)

                else:
                    cipher += chr(ord(text[i])+a)

            elif (ord(text[i]) >= ord('A')) and (ord(text[i])) <= ord('Z'):

                a = int(key[j])
                # print(key[j])
                # print(ord(text[i]))
                if ((ord(text[i])) + a) > 90:
                    modulo = ((ord(text[i]) + a) % 90)
                    while (modulo > 90 or modulo < 64):
                        modulo = (modulo % 90) + 64

                    cipher += chr(modulo)

                else:
                    cipher += chr(ord(text[i]) + a)

            elif (ord(text[i]) >= 32 and (ord(text[i]) < 64)):

                cipher += chr(ord(text[i]) + 1)

            elif(chr(ord(text[i]))=="@"):
                cipher += chr(ord(text[i]))

            elif (ord(text[i]) >= 91 and (ord(text[i]) <= 96)):

                cipher += chr(ord(text[i]))
            # print("In special :", cipher)

            # Now taking care of characters from { which is 123 to ~ which is 126
            elif (ord(text[i]) >= 123 and (ord(text[i]) < 127)):
                cipher += chr(ord(text[i]))


            if (ord(text[i]) <= 31):
                cipher += chr(ord(text[i]))


        elif(not((key[j]).isdigit()) and (not((key[j]).isalpha()))):

            #print("crypting special with not digit not alpha")

            if (ord(text[i]) <= 31):
                cipher += chr(ord(text[i]))

            elif((text[i]).isalpha()):
                bert = (abs(ord(text[i])-3))
                # if(bert<33):
                #     bert += 33
                cipher += chr(bert)

            elif ((text[i]).isdigit()):
                cipher += chr(ord(text[i]))

            else :
                cipher += chr(ord(text[i]))


            # else:
            #
            #     bert = (abs(ord(text[i]) - ord(key[j])))
            #     # print(ord(text[i]))
            #     # print(ord(key[j]))
            #     # Finally got to know the reason why it wasnt displaying. values under 32 can't be printed
            #     # It's values for keys like -> enter,tab,etc
            #     # Hence we add 32 if it's less than 32
            #     if (bert < 33):
            #         bert += 33
            #     #print(bert)
            #     cipher += chr(bert)



        elif(key[j].isalpha()):

            if(text[i].islower()):
                # print(i)
                # print("minisc")

                b = ord(key[j]) - ord('a')
                # A lil twist here is that i'm using 96 instead of 97 so you could still fail the decryption as i'm at -1 char
                # a=97 and z=122, so in case by adding the encryption number to the element of the text
                #we pass 122, pull it back into the range [97-122]
                if(ord(text[i])+b)>122:

                    # In some cases checking only once results in having a number greater than 122 so
                    # I made a loop to make sure that we stay in the range and +96 to start from a
                    modulo=((ord(text[i])+b)%122)+96
                    while(modulo>122):
                        modulo=(modulo%122)+96

                    cipher+=chr(modulo)
                    #print("In small letter :",cipher)
                    # By just doing modulo 122 we'll go back to 1,2,3 etc but ne need to be at least at 97 which is a so we add 96 on top of it
                    #cipher += chr(((ord(text[i])+b)%122)+96)
                else:
                    cipher += chr((ord(text[i])+b))


            elif(text[i].isupper()):

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

            elif (ord(text[i]) <= 31):
                cipher += chr(ord(text[i]))


            elif (ord(text[i]) >= 32 and (ord(text[i]) < 64)):

                    cipher += chr(ord(text[i]) + 1)
            elif(chr(ord(text[i])) =="@"):
                cipher += chr(ord(text[i]))

            elif (ord(text[i]) >= 91 and (ord(text[i]) <= 96)):

                    cipher += chr(ord(text[i]))

            else:

                cipher += chr(ord(text[i]))

        i += 1
        j += 1




                # In this part we make sure that the character inputed is Upperchar





#Now testing the case where the key ain't neither digit nor alpha (letters and numbers)
            # elif (not ((key[j]).isdigit()) and (not ((key[j]).isalpha()))):
            #     bert = (abs(ord(text[i]) - ord(key[j])))
            #     #print(bert)
            #     #Finally got to know the reason why it wasnt displaying. values under 32 can't be printed
            #     #It's values for keys like -> enter,tab,etc
            #     #Hence we add 32 if it's less than 32
            #
            #     if(bert<33):
            #         bert+=33
            #         #print(bert)
            #     cipher += chr(bert)
            #     #print(bert)



            # else:
            #
            #     b = ord(key[j]) - ord('A')
            #     # A=65 and Z=90, so in case by adding the encryption number to the element of the text
            #     # we pass 90, pull it back into the range [65-90]
            #     if (ord(text[i]) + b) > 90:
            #
            #         modulo=((ord(text[i])+b)%90)+64
            #         #In some cases checking only once results in having a number greater than 90 so
            #         #I made a loop to make sure that we stay in the range and +64 to start from A
            #         while(modulo>90):
            #             modulo=(modulo%90)+64
            #         cipher += chr(modulo)


                #     #By just doing modulo 90 we'll go back to 1,2,3 etc but ne need to be at least at 97 which is a so we add 96 on top of it
                #     #cipher += chr(((ord(text[i]) + b) % 90) + 64)
                #
                # else:
                #     cipher += chr((ord(text[i]) + b))
                #     #print(cipher)
                # #print("In Big letter :", cipher)

        # elif (not (text[i]).isdigit()) and (not (text[i]).isalpha):
        #
        #     if (not (key[j]).isdigit()) and (not (key[j]).isalpha):
        #
        #             cipher += chr(ord(text[i]))


        #Now taking care of character from space to @ but i'm not taking care of @ as its value is 64 and there's a possiblity that Uppercase%90=0+64
        #Hence not taking care of @ -> 64

                #print("In Last specials :", cipher)
            #ACTUALLY NO I'LL JUST LEAVE IT AS IT IS


        # else:
        #     cipher += chr(ord(text[i]))
        #     print("In else case :", cipher)





    #print(cipher)
    pyperclip.copy(cipher)

    cipher += "\n\n** SUCCESSFULLY ENCRYPTED --> USE CTRL + V <-- **"



    #Mescod.delete(0.0,END)

    # Make the text box editable
    Mescod.configure(state='normal')

    Mescod.delete(0.0, END)

    Mescod.insert(END,cipher)
    # Text box not editable
    Mescod.configure(state='disabled')


    #God ! I suffered on this one ahaha You gotta set cipher back to empty otherwise it keeps everything in it as it's a global variable
    cipher=""

def cleaner1():
    texto.delete(0.0,END)


def cleaner2():
    Mescod.config(state='normal')
    Mescod.delete(0.0,END)
    Mescod.insert(END, "\n\n Generate the Encrypted/Decrypted message")
    Mescod.config(state='disabled')



root=Tk()
root.title("LASPEED Crypter") #Window Name
root.geometry("700x330") #Window size
root.iconbitmap(r"icones.ico")

img = ImageTk.PhotoImage(Image.open("linkd.png"))
panel = Label(root, image = img)
panel.place(relx=0.8,rely=0.35)
panel.bind("<Button-1>",payp)

img2 = ImageTk.PhotoImage(Image.open("face.jpg"))
panel2 = Label(root, image = img2)
panel2.place(relx =0.8, rely=0.55)
panel2.bind("<Button-1>",faceb)

#imag3 = ImageTk.PhotoImage(Image.open("Linked."))

mess=Label(root,text="Input your Message")
mess.place(relx=.02 , rely=.17)

#This is the textbox in which the text needs to be inputed
texto=Text(root,width=50,height=5,wrap=WORD)

#texto=Entry(root)
texto.place(relx=.2 , rely=.06)

keys=Label(root,text="Enter the key")
keys.place(relx=.43, rely=.35)

#This is the entry box receiving the key
code=Entry(root,show="*")
code.place(relx=.4 , rely=.450)

CLEAN = Button(root,text="CLEAN", command=cleaner1)
CLEAN.place(relx=.83 , rely=.17)

#And this button is supposed to call the crypter function upstairs
crypt=Button(root, text="Encrypt now", command=Crypter, bg="pink")

#crypt.bind("<Button-1>",crypter)
#lambdatest=Button(root,text="OK",command=crypter)
#lambdatest.grid(row=8,column=2)
''' These 3 comments where just some tests to check if the function worked '''
crypt.place(relx=.23 , rely=.50)

Decrypt = Button(root, text="Decrypt now", command=Decrypter, bg="green")
Decrypt.place(relx=.63 , rely=.50)

CLEAN = Button(root,text="CLEAN", command=cleaner2)
CLEAN.place(relx=.83 , rely=.80)

crypted=Label(root,text="RESULT -->")
crypted.place(relx=.03 , rely=.84)



#This is the textbox finally getting the encrypted message

Mescod=Text(root,width=50,height=5,wrap=WORD)
Mescod.insert(END,"\n\n Generate the Encrypted/Decrypted message")

#Here we use configure to make the text box either editable (state='normal') or not editable (state='disable')
Mescod.configure(state='disable')

Mescod.place(relx=.2 , rely=.7)
#Insert here is used to take the take value in the variable coded and insert it in the textbox




root.mainloop()

