def c_word(n):
    if n==1:
        return 'snake'
    elif n==2:
        return 'water'
    else :
        return 'gun'
def check(com_word,low_word):
    if (low_word=='snake' and com_word=='water') or (low_word=='water' and com_word=='gun') or (low_word=='gun' and com_word=='snake') :
        return 1
    else :
        return 0


import random

u_sum=0
c_sum=0
i=0

while(i<5):

    rand=random.randint(1,3)
    # print(rand)
    com_word=c_word(rand)

    word=(input("enter ur choice between (snake ,water ,gun) "))

    low_word=word.lower()
    lis=['snake','water','gun']


    if low_word not in lis :
        print("enter a valid option")
    else :
        
        if low_word==com_word :
            print(f"its a tie! com also chose {com_word}")
        else     :
            i+=1
            if check(low_word,com_word)  :
                c_sum+=1
                print(f"you lost  com chose {com_word}")
            else :
                u_sum+=1
                print(f"u win com chose {com_word}")    



if u_sum>c_sum :
    print(f"u have won the game with a score of {u_sum}:{c_sum} ")
else :
    print(f"u have lost the game with a score of {u_sum}:{c_sum}  ")
           
