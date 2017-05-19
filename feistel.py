'''
    Feistel-Block Implementation
    
    
    This will be used for Blowfish Algorithm. Feistel-Block consists of:
    
    Input: 64 bits message; 48 bits subkey

    partial_message: 32-bit right half from the message 
    partial_result=extend(partial message) xor subkey
    get 8 blocks of info (6 bits each S-BOX) 
    Permuting with the left half of the message.
'''







class Feistel(object):
    def __init__(self):
        pass
    
    def strToBin(self, string):
        return bin(int(binascii,hexlify(str),16))


      



