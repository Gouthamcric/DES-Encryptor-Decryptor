import math
import numpy
def decryption(message,key):
    #Initial permut matrix for the datas
    IP = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    
    #Initial permut made on the key
    PC_1 = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
    
    #Permut applied on shifted key to get Ki+1
    PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
            15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56,
            34, 53, 46, 42, 50, 36, 29, 32]
    
    #Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
    EP = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    
    #SBOX
    S_BOX = [
             
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],  
    
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ], 
    
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ], 
    
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
       
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
    ]
    
    #Permut made after each SBox substitution for each round
    P = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]
    
    #Final permut for datas after the 16 rounds
    IP_1 = [40, 8, 48, 16, 56, 24, 64, 32,
            39, 7, 47, 15, 55, 23, 63, 31,
            38, 6, 46, 14, 54, 22, 62, 30,
            37, 5, 45, 13, 53, 21, 61, 29,
            36, 4, 44, 12, 52, 20, 60, 28,
            35, 3, 43, 11, 51, 19, 59, 27,
            34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25]
    
    #Matrix that determine the shift for each round of keys
    SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    
    
    def hex_to_bin(hex_string):
        bin_string = []
        for i in range(len(hex_string)):
            if(hex_string[i] == '1' or hex_string[i] == 1):
                bin_string.append([0,0,0,1])
            if(hex_string[i] == '2' or hex_string[i] == 2):
                bin_string.append([0,0,1,0])
            if(hex_string[i] == '3' or hex_string[i] == 3):
                bin_string.append([0,0,1,1])
            if(hex_string[i] == '4' or hex_string[i] == 4):
                bin_string.append([0,1,0,0])
            if(hex_string[i] == '5' or hex_string[i] == 5):
                bin_string.append([0,1,0,1])
            if(hex_string[i] == '6' or hex_string[i] == 6):
                bin_string.append([0,1,1,0])
            if(hex_string[i] == '7' or hex_string[i] == 7):
                bin_string.append([0,1,1,1])
            if(hex_string[i] == '8' or hex_string[i] == 8):
                bin_string.append([1,0,0,0])
            if(hex_string[i] == '9' or hex_string[i] == 9):
                bin_string.append([1,0,0,1])
            if(hex_string[i] == 'A' or hex_string[i] == 10):
                bin_string.append([1,0,1,0])
            if(hex_string[i] == 'B' or hex_string[i] == 11):
                bin_string.append([1,0,1,1])
            if(hex_string[i] == 'C' or hex_string[i] == 12):
                bin_string.append([1,1,0,0])
            if(hex_string[i] == 'D' or hex_string[i] == 13):
                bin_string.append([1,1,0,1])
            if(hex_string[i] == 'E' or hex_string[i] == 14):
                bin_string.append([1,1,1,0])
            if(hex_string[i] == 'F' or hex_string[i] == 15):
                bin_string.append([1,1,1,1])
            if(hex_string[i] == '0' or hex_string[i] == 0):
                bin_string.append([0,0,0,0])
    
        return bin_string
    
    def bin_to_dec(bin_string):
        dec = 0
        for i in range(len(bin_string)//2):
            start = 2*i
            stop = 2*(i+1)
            if(bin_string[start:stop] == '00'):
                dec = 0
            if(bin_string[start:stop] == '01'):
                dec = 1
            if(bin_string[start:stop] == '10'):
                dec = 2
            if(bin_string[start:stop] == '11'):
                dec = 3
        return dec
    
    def bin_to_hex(bin_string):
        hex = 0
        for i in range(len(bin_string)//4):
            start = 4*i
            stop = 4*(i+1)
            if(bin_string[start:stop] == '0000'):
                hex = 0
            if(bin_string[start:stop] == '0001'):
                hex = 1
            if(bin_string[start:stop] == '0010'):
                hex = 2
            if(bin_string[start:stop] == '0011'):
                hex = 3
            if(bin_string[start:stop] == '0100'):
                hex = 4
            if(bin_string[start:stop] == '0101'):
                hex = 5
            if(bin_string[start:stop] == '0110'):
                hex = 6
            if(bin_string[start:stop] == '0111'):
                hex = 7
            if(bin_string[start:stop] == '1000'):
                hex = 8
            if(bin_string[start:stop] == '1001'):
                hex = 9
            if(bin_string[start:stop] == '1010'):
                hex = 10
            if(bin_string[start:stop] == '1011'):
                hex = 11
            if(bin_string[start:stop] == '1100'):
                hex = 12
            if(bin_string[start:stop] == '1101'):
                hex = 13
            if(bin_string[start:stop] == '1110'):
                hex = 14
            if(bin_string[start:stop] == '1111'):
                hex = 15
    
        return hex
    
    def expansion_permutation(x):
        y = [0]*48
        for i in range(len(y)):
            y[i] = x[EP[i]-1] 
    
        return y
    
    def initial_permutation(x):
        y = [0]*64
        for i in range(64):
            y[i] = x[IP[i]-1]
    
        return y
    
    def permutation_choice_1(x):
        y = [0]*56
        for i in range(56):
            y[i] = x[PC_1[i]-1]
        
        return y
    
    def permutation_choice_2(x):
        y = [0]*48
        for i in range(48):
            y[i] = x[PC_2[i]-1]
        
        return y
    
    def permutation(x):
        y = [0]*32
        for i in range(32):
            y[i] = x[P[i]-1]
        
        return y
    
    def listToString(s):  
        str1 = ""  
         
        for ele in s:  
            str1 += str(ele)   
           
        return str1  
    
    def XOR_operation(x,y):
        res = [0]*len(x)
        for i in range(len(x)):
            if(x[i] == y[i]):
                res[i] = 0
            else:
                res[i] = 1
        
        return res   
    
    def rotate(l, n):
        return l[n:] + l[:n]    
    
    print("Initial Calculation")
    
    def inverse_permutation(x):
        y = [0]*64
        for i in range(64):
            y[i] = x[IP_1[i]-1]
        
        return y
    
    
    # Initialising hex string
    M = message
    K = key
    L = [[0]*32]*17
    R = [[0]*32]*17
    C = [0]*17
    D = [0]*17
    Key = [[0]*48]*17
    # Printing initial string 
    print ("Message", M)
    print ("Pass Key", K)
    
    
    ################################ Message #############################
    
    M_bin = hex_to_bin(M)
    M_bin = [j for sub in M_bin for j in sub]
    print("Plain plain text to binary :" , M_bin)
    
    res_pt = initial_permutation(M_bin)
    print("After initial permutation :" , res_pt)
    
    L[0] = res_pt[0:32]
    R[0] = res_pt[32:64]
    print("L0 : ", L[0])
    print("R0 : ", R[0])
    
    res_pt = expansion_permutation(R[0])
    print(res_pt)
    ##################################################################
    
    
    ################################ Key #############################
    
    K_bin = hex_to_bin(K)
    K_bin = [j for sub in K_bin for j in sub]
    print ("Key to binary", str(K_bin))
    
    res_k = permutation_choice_1(K_bin)
    print("After permutation choice 1 :" , res_k)
    
    C[0] = res_k[0:28]
    D[0] = res_k[28:56]
    print("C0 : ", C[0])
    print("D0 : ", D[0]) 
    ###################################################################
    
    
    
    for i in range(16):
        # Key Generation
        print("Round" ,i+1)
        print("\n")
    
        print("Key generation")
        C[i+1] = rotate(C[i],SHIFT[i])
        D[i+1] = rotate(D[i],SHIFT[i])
        print("C : ", C[i+1])
        print("D : ", D[i+1]) 
        
        Key[i+1] = permutation_choice_2(C[i+1] + D[i+1])
        print("Key", Key[i+1])
    
    
        print("\n")
    
    for i in range(16):
        print("Round" ,i+1)
        print("\n")
    
        # Cipher Text Generation
        print("Cipher Text generation")
        tmp_pt = expansion_permutation(R[i])
        print("After Expansion", tmp_pt)
    
        tmp_pt = XOR_operation(Key[16-i],tmp_pt)
        print("After K XOR E(R)",tmp_pt)
    
        SBOX_res = []
        for j in range(0,len(tmp_pt)//6):
            start = 6*j
            stop = 6*(j+1)
            tmp_s = listToString(tmp_pt[start:stop])
            row = bin_to_dec(tmp_s[0:6:5])
            col = bin_to_hex(tmp_s[1:5])
            SBOX_res.append(S_BOX[j][row][col])
        print("SBOX Application", SBOX_res)
    
        SBOX_res = hex_to_bin(SBOX_res)
        print("SBOX Result to Binary", SBOX_res)
    
        SBOX_res = [j for sub in SBOX_res for j in sub]
        Permutation_res = permutation(SBOX_res)
        print("Result after Permutation", Permutation_res)
    
        R[i+1] = XOR_operation(L[i],Permutation_res)
        print("R", R[i+1])
    
        L[i+1] = R[i]
        print("L", L[i+1])
    
        print("\n\n")
    
    result = inverse_permutation(R[16]+L[16])
    print("Final Answer" , result)
    print("Hexadecimal Format",hex(int(listToString(result), 2)))
    return (hex(int(listToString(result), 2)))
    
    
