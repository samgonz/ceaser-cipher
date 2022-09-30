
def encodeMessage(message, shift_number):
    for i in message:
      message = message.replace(i, chr(ord(i) + shift_number))
    return message
  
def decodeMessage(message, shift_number):
    for i in message:
      message = message.replace(i, chr(ord(i) - shift_number))
    return message