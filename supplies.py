'''
Supplies for ThreeFish 
Encription

'''

import binascii


class Supplies(object):
    #Rotate Left
    rol = lambda val, r_bits, max_bits: \
                (val << r_bits%max_bits) & (2**max_bits-1) | \
                    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
    
    def __init__(self):
        self.setRotationTable()
        self.dCounter=0
        self.wCounter=0

    def setRotationTable(self):
        self.rotationTable=[[0 for x in range(8)] for y in range(8)]
        
        self.rotationTable[0][0]=38
        self.rotationTable[0][1]=30
        self.rotationTable[0][2]=50
        self.rotationTable[0][3]=53
        
        self.rotationTable[1][0]=48
        self.rotationTable[1][1]=20
        self.rotationTable[1][2]=43
        self.rotationTable[1][3]=31
        
        self.rotationTable[2][0]=34
        self.rotationTable[2][1]=14
        self.rotationTable[2][2]=15
        self.rotationTable[2][3]=27
        
        self.rotationTable[3][0]=26
        self.rotationTable[3][1]=12
        self.rotationTable[3][2]=58
        self.rotationTable[3][3]=7
           
        self.rotationTable[4][0]=33
        self.rotationTable[4][1]=49
        self.rotationTable[4][2]=8
        self.rotationTable[4][3]=42
         
        self.rotationTable[5][0]=39
        self.rotationTable[5][1]=27
        self.rotationTable[5][2]=41
        self.rotationTable[5][3]=14
         
        self.rotationTable[6][0]=29
        self.rotationTable[6][1]=26
        self.rotationTable[6][2]=11
        self.rotationTable[6][3]=9
         
        self.rotationTable[7][0]=33
        self.rotationTable[7][1]=51
        self.rotationTable[7][2]=39
        self.rotationTable[7][3]=35

    def getBlockList(self, bString, blocksize):                            
        rt=[bString[i:i+64] for i in range(0, len(bString), 64)]
        for i in range( len(rt) ):
            if(len(rt[i])<64):
                rt[i] = rt[i].ljust(blocksize,'0')
        
        return rt 
    
    def getBinString(self, param):
        return bin(int(binascii.hexlify(param.encode()), 16))[2:]

    def xorAll(self, strList):
        rt=strList[0]
        for i in range(1, len(strList)):
            rt^=i
        return rt



    def mixFunction(self, w0, w1):
        rt=[]
        rt.append((w0+w1)%(2**64))
        rt.append(self.rol(w1,self.rotationTable[self.dCounter%8][j],))
