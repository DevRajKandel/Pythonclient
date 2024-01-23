
import requests

infpParm1 = input("Enter A,B,C")
#webbrowser.open("https://devkandel1034.000webhostapp.com/Second.php?q="+inpParm1,0,True)
# 2) HTTP Request to  the Server
# Sends a get Request
xlam = requests.get("https://devkandel1034.000webhostapp.com/Second.php?q="+infpParm1)
print(xlam.text)
input("Enter a key to exit")
# Making GET Requests...3
"""  """