import random
import pandas as pd
import numpy as np
import openpyxl
import os

def dice(number):
    throws = [random.randint(1, 6) for i in range(number)]
    # throws = list(())
    # for i in range(number):
    #    a = random.randint(1,6)
    #    throws.append(a)
    # print(throws)
    return throws

def tablename(name):
    path = r"C:\Users\\arong\OneDrive\Dokumente\Desktop\Python\Risikotabellen" '\\'
    ending = '.xlsx'
    result = path + name + ending
    return result


class Attack:

    def __init__(self, attack_armys, defend_armys, attarmys, defarmys,  rounds):
        self.attack_armys = attack_armys
        self.defend_armys = defend_armys
        self.attarmys = attarmys
        self.defarmys = defarmys
        self.rounds = rounds

    def store_variables(self): # Restore the variables self.attack_armys and self.defend_armys after every fight
        self.attack_armys = self.attarmys
        self.defend_armys = self.defarmys

    def round(self): # One throw of both parties + comparison of the results

        if self.attack_armys >= 3: # Set attacker throws
            attack_throws = 3
        else:
            attack_throws = self.attack_armys

        attack_result = dice(attack_throws) # attack random dice#

        # print('a', attack_throws, attack_result)

        if self.defend_armys >= 2: # Set defender throws
            defend_throws = 2
        else:
            defend_throws = 1

        defend_result = dice(defend_throws) # defend random dice

        # print('d', defend_throws, defend_result)

        attack_result.sort(reverse=True)
        defend_result.sort(reverse=True)

        if len(defend_result) < len(attack_result): # Set x for result comparison
            x = len(defend_result) - 1
        else:
            x = len(attack_result) - 1

        while x >= 0: # Compare results and kill Armies

            if attack_result[x] > defend_result[x]:
                self.defend_armys -= 1
            else:
                self.attack_armys -=1

            x -= 1


    def show(self):

        print(f'Attacker has {self.attack_armys} armys and defender has {self.defend_armys} armys')


    def fight(self):

        # print(f'The attacker attacks with {self.attack_armys} and the defender defends with {self.defend_armys} armys')

        rounds = 0
        self.store_variables()

        while self.defend_armys > 0 and self.attack_armys > 0:
            self.round()
            rounds += 1

        if self.attack_armys == 0:
            return 0
        elif self.defend_armys == 0:
            return 1

        print(self.attack_armys, self.defend_armys)

        # print(f'The attacker has left {self.attack_armys} and the defender has left {self.defend_armys} armys \nIt took {rounds} rounds')


    def multi_round(self):

        rounds_won = 0
        rounds_lost = 0


        for i in range(1, self.rounds + 1):

            # print(i)

            a = self.fight()


            if a == 1:
                rounds_won +=1
            if a == 0:
                rounds_lost += 1

            # print('round over')

        return rounds_won, rounds_lost

'''
x = int(input('How many attack armys? '))
y = int(input('How many defend armys? '))
z = int(input('And how many rounds? '))

a = Attack(x, y, x, y, z)

prob = a.multi_round()[0] / z * 100
round_prob = round(prob, 2)

print(f'Your probability of winning against {y} defending armies with {x} attacking armies is {round_prob}%')



'''
x = int(input('How many attacking armies should I try out? '))
y = int(input('How many defending armies should I try out? '))
z = int(input('How many simulations per scenario? '))

probtable = dict()

for i in range(1, x+1):
    probtable[i] = []
    for j in range(1, y+1):
        a = Attack(i, j, i, j, z)
        probtable[i].append(round(a.multi_round()[0] / z * 100, 2))

df = pd.DataFrame(probtable, index=range(1, y+1))

print(df)

t = 1
while t == 1:
    export = input('Do you want your table to be made an excel file? ')
    if export == 'yes':
        uname = input('Enter the file name: ')
        path = tablename(uname)
        df.to_excel(path)
        t = 0
    elif export == 'no':
        break
    else:
        print('Please enter \"yes\" or \"no\".')

