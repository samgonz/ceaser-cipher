import encrypterDecrypter
 
encrypt_or_decrypt = input('Type [encode] to encode a message and [decode] to decode a message.\n').lower()

if encrypt_or_decrypt == 'encode':
  encoded_message = input('Please type the message you would like to encode:\n').lower()
  decrypted_message = encoded_message
  shift_number = int(input('How much would you like to shift your message by?\n')) 
  test = chr(ord('i') + shift_number)
  
  decrypted_message = encrypterDecrypter.encodeMessage(decrypted_message, shift_number)
    
  print(f'Here is the encoded message, {decrypted_message}')

elif encrypt_or_decrypt == 'decode':
  decrypted_message = input('Please type the message you would like to decode:\n').lower()
  encoded_message = decrypted_message
  shift_number = int(input('How much would you like to shift your message by?\n')) 
  test = chr(ord('i') + shift_number)
  
  encoded_message = encrypterDecrypter.decodeMessage(encoded_message, shift_number)
    
  print(f'Here is the decoded message, {encoded_message}')