"""
    This is an attempted test at a encryption porgram using 
    one of the apporoaches:
    - encrypt using ascii code
    - encrypt using string reversal
    - symmetric key encryption
    
    
    Please Note: The Colon indicates the type of data we expect,
    this is a Python annotation. Like in JUNIT tests...
"""

# Encrypt Function for AScII Code
# chr() turns int to char
# ord turns char to int
def ascii_encrypt():
    msg: str = input("enter message to encrypt: ")
    msg_length: int = len(msg)
    msg_array: int = []
    count: int = 0 # test variable for items in array
    msg_encrypt: str = ""
    for character in msg:
        ascii_number = ord(character) + 5
        # 5 has been added to ASCII Transformation as this is the key
        hex_number = hex(ascii_number)
        msg_encrypt += hex_number
        # print(msg_encrypt) - Testing Output
    
    return msg_encrypt

howdy = ascii_encrypt()
print(howdy)