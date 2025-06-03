encrypted = []
text=""  #eskiden flag buradaydı
key=     #0-1000 arasında rastgele bir key seçtim
for char in text:
    encrypted_char = ord(char) ^ key
    encrypted.append(encrypted_char)
print(encrypted)

#encrypted flag=[183, 174, 179, 168, 164, 179, 161, 188, 191, 168, 181, 189, 168, 181, 163, 162, 160, 174, 171, 186]
