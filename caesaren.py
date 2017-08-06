
message = str(raw_input("Enter message.."))
key = int(raw_input("Enter key.."))

encrypted_list = []
encrypted_text = ''
temp = 0


#for i in range(0,len(message)):
for i in message:
    if i >= 'a' and i <= 'z':
        temp = ord(i) + key
        if temp > ord('z'):
            temp = ord(i) - ord('z') + ord('a') - 1
            temp = temp + key
        encrypted_list.append(chr(temp))
    elif i >= 'A' and i <= 'Z':
        temp = ord(i) + key
        if temp > ord('Z'):
            temp = ord(i) - ord('Z') + ord('A') - 1
            temp = temp + key
        encrypted_list.append(chr(temp))

encrypted_text = ''.join(encrypted_list)
print encrypted_text
        
            



