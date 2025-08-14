# Original string
text = "Hello, world! 🌍"

# UTF-8 encoding
utf8_bytes = text.encode('utf-8')
print("UTF-8:", utf8_bytes)

# UTF-16 encoding
utf16_bytes = text.encode('utf-16')
print("UTF-16:", utf16_bytes)

# UTF-32 encoding
utf32_bytes = text.encode('utf-32')
print("UTF-32:", utf32_bytes)

# Decoding back to string
print("Decoded UTF-8:", utf8_bytes.decode('utf-8'))
print("Decoded UTF-16:", utf16_bytes.decode('utf-16'))
print("Decoded UTF-32:", utf32_bytes.decode('utf-32'))

def decode_utf8_bytes_to_str_wrong(bytestring: bytes): 
    return "".join([bytes([b]).decode("utf-8") for b in bytestring]) 

#print(decode_utf8_bytes_to_str_wrong("hello! こんにちは!".encode("utf-8"))) 
print('hello! こんにちは!'.encode("utf-8"))



