########################################################################
##
## CS 101 Lab
## Program # 3
## Name- Hedieh Tavallali
## Email- httnm@umsystem.edu
##
## PROBLEM : create many types of loops with some that are nested in others

##
## ALGORITHM :

print("Welcome to the Flarsheim Gusser!\n")

while(True):
    print("Please think of a number between and including 1 and 100.\n")
    
    values="357"
    
    res=[]
    for i in values:
        while(True):
            print("What is the remainder when your number is divide by ",i," ?",end="")
            r=int(input())
            if(r<0):
                print("The value entered must be 0 or greater")
                continue
            elif(r>=int(i)):
                print("The value entered must be less than ",i)
                continue
            else:
                if(i!='7'):
                    print()
                res.append(r)
                break
    
    for val in range(1,101):
        if(val%3 == res[0] and val%5 == res[1] and val%7 == res[2]):
            print("Your number was ",str(val))
            print("How amazing is that?\n")
            break

    
    choice=''
    while(True):
        print("Do you want to play the game again?Y to continue,N to quit ==> ",end="")
        choice=input()
        if(choice=='n' or choice=='N' or choice=='y' or choice=='y'):
            break
        else:
            continue
        
    if(choice=='n' or choice=='N'):
        break
    elif(choice=='y' or choice=='Y'):
        print()
        continue


##      
## 
## ERROR HANDLING:
##   I ran into a few indentation errors but they were easily fixable
##
## OTHER COMMENTS:
##      N/A
##
########################################################################
