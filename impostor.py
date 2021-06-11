#random prnt.sc link gen
#dont be sussy amongus impostor
import webbrowser
import string
import random
numberoflinks = 0


linknumber = float(input('how many links would you like'))

while linknumber != numberoflinks:

  randomstring = ''.join(random.choices(string.ascii_lowercase+string.digits, k = 6))

  webbrowser.open_new_tab('https://prnt.sc/'+str(randomstring))


  numberoflinks += 1


if numberoflinks == linknumber:
  print("All requested links have been opened!")

userfeedback = float(input("How many of your image links were missing?"))
if userfeedback < 1:
  print("Good!")
  exit()

elif userfeedback > linknumber:
  print("Fat liar impostor give me an accurate number")

elif userfeedback <= linknumber:
  yn = input("Would you like to start again y/n")
  if yn == ('n'):
    exit()
  if yn == ('y'):
    numberoflinks1 = 0
    linknumber1 = float(input('how many links would you like'))

    while linknumber1 != numberoflinks1:
      randomstring1 = ''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=6))

      webbrowser.open_new_tab('https://prnt.sc/' + str(randomstring1))
      print('https://prnt.sc/' + str(randomstring1))

      numberoflinks1 += 1

  if numberoflinks1 == linknumber1:
    print("All requested links have been opened!")
    exit()
