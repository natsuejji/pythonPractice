# -- coding: utf-8 --
import random
def guess_number():
    target_number = random.randint(1,999)
    loop = True
    while loop:
        try:
            try_number = int(input('please input a number between 1 and 999:'))
        except:
            print('game over')
            break
        
        if try_number == target_number:
            loop = False
            print ('win')
        elif try_number > target_number:
            print ('Greater than target')
        elif try_number < target_number:
            print ('Less than target')
        
if __name__ == '__main__':
    guess_number()