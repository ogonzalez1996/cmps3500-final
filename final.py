#arrays to print in a spiral path
ar =[
      [1, 2],
      [5, 0]
    ]

def Menu():
    loop = True
    while loop:
        try:
            print_menu()
            selection = int(input("Enter Choice: "))
            if selection==1:
                spiral_path(ar)
            elif selection==2:
                num = int(input("Enter number: "))
                Moran(num)
            elif selection ==3:
                shortWord()
            elif selection==4:
                res = int(input("Enter a number to convert to string: "))
                j = numtoword(res)
                print (j)
            elif selection==5:
                print ("goodbye!")
                loop = False
            else:
                print ("invalid choice number from 1-5")
        except ValueError:  
             print("Invalid input chose a number between 1-5")

def print_menu():
    print ("1. Print 2D array in a spiral path")
    print ("2. Determine whether a number is a Harshad number, Moran Number or neither")
    print ("3. Determine the shortest word in a sentence")
    print ("4. Turn a number into a word(s)")
    print ("5. Exit from the program")
#helper function for determining Moran Numbers
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def spiral_path(ar):

    print (ar) 
    rows, cols = len(ar), len(ar[0])
    r, c = 0, -1 # start here
    nextturn = stepsx = cols # move so many steps
    stepsy = rows-1
    inc_c, inc_r = 1, 0 # at each step move this much
    turns = 0 # how many times our snake had turned
    for i in range(rows*cols):
        c += inc_c
        r += inc_r 

        print (ar[r][c], end = " ")

        if i == nextturn-1:
            turns += 1
            # at each turn reduce how many steps we go next
            if turns%2==0:
                nextturn += stepsx
                stepsy -= 1
            else:
                nextturn += stepsy
                stepsx -= 1
            # change directions
            inc_c, inc_r = -inc_r, inc_c  
    print("\n")

def Moran(input):
    num = input;    
    rem = sum = 0;    
     
    #Make a copy of num and store it in variable n    
    n = num;    
     
    #Calculates sum of digits    
    while(num > 0):    
        rem = num%10;    
        sum = sum + rem;    
        num = num//10;    
     
    #Checks whether the number is divisible by the sum of digits    
    if((n%sum == 0) and not isprime(n/sum)):    
        print(str(n) + " ==> H")
    elif((n%sum == 0) and isprime(n/sum)):    
        print(str(n) + " ==> M")

    else:    
        print(str(n) + " ==> Neither"); 

def shortWord():
    sent = input("Enter sentence to determine shortest word: ")
    words =  sent.split()
    m = min(words, key=len)
    print("The shortest word is " + m)

def numtoword(num):  
    under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    above_100 = {100: 'Hundred'}
    if (num > 999 or num < 0):
       return "out of bounds - chose something between 0 and 999"
    if num < 20:
       return under_20[num]
    if num < 100:
       return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[num%10])
    	# append the pivot - 'Hundred;
    pivot = max([key for key in above_100.keys() if key <= num])
     
    return numtoword((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + numtoword(num%pivot))
Menu()
