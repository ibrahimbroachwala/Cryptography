
message = str(raw_input("Enter message.."))
key = int(raw_input("Enter key.."))

decrypted_list = []
decrypted_text = ''
temp = 0


#for i in range(0,len(message)):
for i in message:
    if i >= 'a' and i <= 'z':
        temp = ord(i) - key
        if temp < ord('a'):
            temp = ord(i) + ord('z') - ord('a') + 1
            temp = temp - key
        decrypted_list.append(chr(temp))
    elif i >= 'A' and i <= 'Z':
        temp = ord(i) - key
        if temp < ord('A'):
            temp = ord(i) + ord('Z') - ord('A') + 1
            temp = temp - key
        decrypted_list.append(chr(temp))

decrypted_text = ''.join(decrypted_list)
print decrypted_text
        
            

