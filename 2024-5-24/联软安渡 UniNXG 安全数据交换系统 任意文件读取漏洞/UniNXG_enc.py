import base64


def encode_string(string):
    bytes_ = bytearray(string, 'utf-8')
    result = bytearray(len(bytes_))
    for i in range(len(bytes_)):
        if i % 2 != 0:
            result[i] = bytes_[i] - 2
        else:
            result[i] = (bytes_[i] - 3) ^ 73

    s = result.decode('utf-8')
    encoded_string = base64.b64encode(s.encode('utf-8'))
    return encoded_string.decode('utf-8')


def decode_string(encoded_string):
    decoded_string = base64.b64decode(encoded_string)
    decoded_string = decoded_string.decode('utf-8')

    result = bytearray(len(decoded_string))
    for i in range(len(decoded_string)):
        if i % 2 != 0:
            result[i] = ord(decoded_string[i]) + 2
        else:
            result[i] = (ord(decoded_string[i]) ^ 73) + 3

    return result.decode('utf-8')


# 加密功能
def encrypt():
    original_string = input("请输入要加密的字符串：")
    encoded_string = encode_string(original_string)
    print("加密后的字符串:", encoded_string)


# 解密功能
def decrypt():
    encoded_string = input("请输入要解密的字符串：")
    decoded_string = decode_string(encoded_string)
    print("解密后的字符串:", decoded_string)


# 主程序
while True:
    choice = input("请选择操作（1.加密 2.解密 3.退出）：")
    if choice == '1':
        encrypt()
    elif choice == '2':
        decrypt()
    elif choice == '3':
        break
    else:
        print("无效的选择，请重新输入。")
