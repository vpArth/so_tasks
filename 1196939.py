import base64

inputData = [1, 1108, 4512, 1, 2554, 2207, 3125, 7];
wordList = [num.to_bytes(2, byteorder='big') for num in inputData]

encoded = b''.join(wordList); # b'\x00\x01\x04T\x11\xa0\x00\x01\t\xfa\x08\x9f\x0c5\x00\x07'
b64encoded = base64.b64encode(encoded).decode('ascii')
print(base64.b64encode(encoded).decode('ascii'))


byte_str = base64.b64decode(b64encoded)
restored = [int.from_bytes(byte_str[i:i+2], byteorder='big') for i in range(0, len(byte_str), 2)]
print(restored)
