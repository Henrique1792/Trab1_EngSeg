'''
Supplies for ThreeFish 
Encription

'''

import binascii


class Supplies(object):
    rotationTable=None
    def __init__(self):
        self.setRotationTable()

    def setRotationTable(self):
        self.rotationTable=[[0 for x in range(8)] for y in range(8)]
        
        rotationTable[0][0]=55
        rotationTable[0][1]=43
        rotationTable[0][2]=37
        rotationTable[0][3]=40
        rotationTable[0][4]=16
        rotationTable[0][5]=22
        rotationTable[0][6]=38
        rotationTable[0][7]=12
        
        rotationTable[1][0]=25
        rotationTable[1][1]=25
        rotationTable[1][2]=46
        rotationTable[1][3]=13
        rotationTable[1][4]=14
        rotationTable[1][5]=13
        rotationTable[1][6]=52
        rotationTable[1][7]=57
        
        rotationTable[2][0]=33
        rotationTable[2][1]=8
        rotationTable[2][2]=18
        rotationTable[2][3]=57
        rotationTable[2][4]=21
        rotationTable[2][5]=12
        rotationTable[2][6]=32
        rotationTable[2][7]=54
        
        rotationTable[3][0]=34
        rotationTable[3][1]=43
        rotationTable[3][2]=25
        rotationTable[3][3]=60
        rotationTable[3][4]=44
        rotationTable[3][5]=9
        rotationTable[3][6]=59
        rotationTable[3][7]=34
        
        rotationTable[4][0]=28
        rotationTable[4][1]=7
        rotationTable[4][2]=47
        rotationTable[4][3]=48
        rotationTable[4][4]=51
        rotationTable[4][5]=9
        rotationTable[4][6]=35
        rotationTable[4][7]=41
        
        rotationTable[5][0]=17
        rotationTable[5][1]=6
        rotationTable[5][2]=18
        rotationTable[5][3]=25
        rotationTable[5][4]=43
        rotationTable[5][5]=42
        rotationTable[5][6]=40
        rotationTable[5][7]=15
        
        rotationTable[6][0]=58
        rotationTable[6][1]=7
        rotationTable[6][2]=32
        rotationTable[6][3]=45
        rotationTable[6][4]=19
        rotationTable[6][5]=18
        rotationTable[6][6]=2
        rotationTable[6][7]=56
        
        rotationTable[7][0]=47
        rotationTable[7][1]=49
        rotationTable[7][2]=27
        rotationTable[7][3]=58
        rotationTable[7][4]=37
        rotationTable[7][5]=48
        rotationTable[7][6]=53
        rotationTable[7][7]=56



    def getBinString(self, string):
        return bin(int(binascii.hexlify(string),16))
