import binascii

'''
About Tables:
    PC1 will be used only on first round - all subsequent uses pc2

    first, second and 16th round - shift 1 to get next subkey
    rest of them - shift 2
'''
class Tables(self):
    expansionTable =[[0 for x in range(6)] for y in range(8)]
    PC1=[[0 for x in range(8)]for y in range(7)]
    PC2=[[0 for x in range(8)]for y in range(6)]
    def __init__(self):
        self.setExpansionTable()
        self.setPCTables()


    def setExpansionTable(self):
        self.expansionTable[0][0]=32
        self.expansionTable[0][1]=1
        self.expansionTable[0][2]=2
        self.expansionTable[0][3]=3
        self.expansionTable[0][4]=4
        self.expansionTable[0][5]=5
       
        self.expansionTable[1][0]=4
        self.expansionTable[1][1]=5
        self.expansionTable[1][2]=6
        self.expansionTable[1][3]=7
        self.expansionTable[1][4]=8
        self.expansionTable[1][5]=9
      
        self.expansionTable[2][0]=8
        self.expansionTable[2][1]=9
        self.expansionTable[2][2]=10
        self.expansionTable[2][3]=11
        self.expansionTable[2][4]=12
        self.expansionTable[2][5]=13
        
        self.expansionTable[3][0]=12 
        self.expansionTable[3][1]=13
        self.expansionTable[3][2]=14
        self.expansionTable[3][3]=15
        self.expansionTable[3][4]=16
        self.expansionTable[3][5]=17

        self.expansionTable[4][0]=16
        self.expansionTable[4][1]=17
        self.expansionTable[4][2]=18
        self.expansionTable[4][3]=19
        self.expansionTable[4][4]=20
        self.expansionTable[4][5]=21
       
        self.expansionTable[5][0]=20
        self.expansionTable[5][1]=21
        self.expansionTable[5][2]=22
        self.expansionTable[5][3]=23
        self.expansionTable[5][4]=24
        self.expansionTable[5][5]=25
        
       
        self.expansionTable[6][0]=24
        self.expansionTable[6][1]=25
        self.expansionTable[6][2]=26
        self.expansionTable[6][3]=27
        self.expansionTable[6][4]=28
        self.expansionTable[6][5]=29
       
        self.expansionTable[7][0]=28
        self.expansionTable[7][1]=29
        self.expansionTable[7][2]=30
        self.expansionTable[7][3]=31
        self.expansionTable[7][4]=32
        self.expansionTable[7][5]=1


    def setPCTables(self):
        #Pc1Table
        self.PC1[0][0]=57
        self.PC1[0][1]=49
        self.PC1[0][2]=41
        self.PC1[0][3]=33
        self.PC1[0][4]=25
        self.PC1[0][5]=17
        self.PC1[0][6]=9
        
        self.PC1[1][0]=1
        self.PC1[1][1]=58
        self.PC1[1][2]=50
        self.PC1[1][3]=42
        self.PC1[1][4]=34
        self.PC1[1][5]=26
        self.PC1[1][6]=18
        
        self.PC1[2][0]=10
        self.PC1[2][1]=2
        self.PC1[2][2]=59
        self.PC1[2][3]=51
        self.PC1[2][4]=43
        self.PC1[2][5]=35
        self.PC1[2][6]=27
        
        self.PC1[3][0]=19
        self.PC1[3][1]=11
        self.PC1[3][2]=3
        self.PC1[3][3]=60
        self.PC1[3][4]=52
        self.PC1[3][5]=44
        self.PC1[3][6]=36
        
        self.PC1[4][0]=63
        self.PC1[4][1]=55
        self.PC1[4][2]=47
        self.PC1[4][3]=39
        self.PC1[4][4]=31
        self.PC1[4][5]=23
        self.PC1[4][6]=15
        
        self.PC1[5][0]=7
        self.PC1[5][1]=62
        self.PC1[5][2]=54
        self.PC1[5][3]=46
        self.PC1[5][4]=38
        self.PC1[5][5]=30
        self.PC1[5][6]=22
        
        self.PC1[6][0]=14
        self.PC1[6][1]=6
        self.PC1[6][2]=61
        self.PC1[6][3]=53
        self.PC1[6][4]=45
        self.PC1[6][5]=37
        self.PC1[6][6]=29
        
        self.PC1[7][0]=21
        self.PC1[7][1]=13
        self.PC1[7][2]=5
        self.PC1[7][3]=28
        self.PC1[7][4]=20
        self.PC1[7][5]=12
        self.PC1[7][6]=4
        
        #Pc1Table
        
        #Pc2Table
        self.PC2[0][0]=14
        self.PC2[0][1]=17
        self.PC2[0][2]=11
        self.PC2[0][3]=24
        self.PC2[0][4]=1
        self.PC2[0][5]=5
        
        self.PC2[1][0]=3
        self.PC2[1][1]=28
        self.PC2[1][2]=15
        self.PC2[1][3]=6
        self.PC2[1][4]=21
        self.PC2[1][5]=10
        
        self.PC2[2][0]=23
        self.PC2[2][1]=19
        self.PC2[2][2]=12
        self.PC2[2][3]=4
        self.PC2[2][4]=26
        self.PC2[2][5]=8
        
        self.PC2[3][0]=16
        self.PC2[3][1]=7
        self.PC2[3][2]=27
        self.PC2[3][3]=20
        self.PC2[3][4]=13
        self.PC2[3][5]=2
        
        self.PC2[4][0]=41
        self.PC2[4][1]=52
        self.PC2[4][2]=31
        self.PC2[4][3]=37
        self.PC2[4][4]=47
        self.PC2[4][5]=55
        
        self.PC2[5][0]=30
        self.PC2[5][1]=40
        self.PC2[5][2]=51
        self.PC2[5][3]=45
        self.PC2[5][4]=33
        self.PC2[5][5]=48
        
        self.PC2[6][0]=44
        self.PC2[6][1]=49
        self.PC2[6][2]=39
        self.PC2[6][3]=56
        self.PC2[6][4]=34
        self.PC2[6][5]=53
        
        self.PC2[7][0]=46
        self.PC2[7][1]=42
        self.PC2[7][2]=50
        self.PC2[7][3]=36
        self.PC2[7][4]=29
        self.PC2[7][5]=32
        
        
        #Pc2Table

class sBox(object):
    sTable=None
    def __init__(self):
        self.sTable=[[0 for x in range(4)]for y in range(14)]
