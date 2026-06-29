hex_input = input("Enter hex string: ")
text = bytes.fromhex(hex_input).decode('utf-8')
print(text)
