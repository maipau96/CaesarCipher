from anvil import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    
 
    

    # Any code you write here will run when the form opens.

  def button_1_click (self, **event_args):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newMessage = ''
    message = self.raw.text
    key= int(self.keyNum.text)
    for character in message:
      if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
      else:
        newMessage += character
    self.encrypted.text=newMessage
    pass
