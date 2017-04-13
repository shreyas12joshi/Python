#Developed by Anant, Narra and Shreyas
#Program for finding square root of a number
import sys


def square(Num):
    
    for i in range(0,Num):
        result = i*i
        if result > Num:
            i = i-1            
            return i
        elif result == Num:
            print ('The square root of %d is %d' %(Num, i))
            square_root()
            sys.exit()

def square_root():
    str1 = 'Y'
    while (str1 == 'Y'):
        
        print 'Enter the number'
        Num = int(raw_input())
        if Num < 1:
            print 'Chutiya detected'
            sys.exit()
        num_square = square(Num)

        SQUARE_ROOT = num_square #7
        d = Num - (num_square * num_square)     #4
        num_square = num_square * 2     #14
        k = 0
        d = d * 100 #400
        temp = 0
        for n in range (1,10):
            
            num_square = num_square*10 #140, 1440, 14560, 145600
            
            if((d<num_square)):                
                temp = 1
                
            j = 0
            i1 = 1
            num_square1 = num_square #140, 1448
            if temp == 0:
                j=1    
                while (i1 < d):
                    
                    i1 = (num_square1 + j)*j
                    
                    j = j+1
                    

                j = j-2     #2, 8
            temp = 0  
            SQUARE_ROOT = (SQUARE_ROOT *10) + j     #72, 728, 7280
            num_square = (num_square + j)  #142, 1448, 14560

            d = d - (num_square*j) #116, 16, 1600
            num_square = num_square + j     #144, 1456, 14560
            
            d = d * 100 #11600, 1600, 160000



        SQUARE_ROOT = SQUARE_ROOT/(10.0**(n))
        #SQUARE_ROOT = round(SQUARE_ROOT,4)
        print ('The square root of %d is %.9f' %(Num, SQUARE_ROOT))    
        print 'Do you wnat to ontinue (Y/N)'
        str1 = raw_input()


    print 'DONE'

 
##while (str1 == 'Y'):
##    print 'Enter the number'
##    Num = int(raw_input())
##    if Num < 1:
##        print 'Chutiya detected'
##
##    print 'Do you wnat to ontinue (Y/N)'
    
square_root() 
