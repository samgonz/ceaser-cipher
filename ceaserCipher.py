encrypt_or_decrpyt = input('Type [encode] to encode a message and decrpyt [decrypt] to decrypt a message.').lower()

if encrypt_or_decrypt == 'encode':
  unencrypted_message = input('Please type the message you would like to encrpyt').lower()
  shift_number = int(input('How much would you like to shift your message by?')) 
  
  for i in unencrypted_message:
    encrypted_message = chr (ord (i) + shift_number)
    
  print(f'Here is the encrypted message, {encrypted_message}')
