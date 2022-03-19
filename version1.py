import easygui
import numpy as np
from random import seed
from random import randint

#get input from the user
inputNames = easygui.enterbox("please enter the names (separate with space)")
inputNoTeams = easygui.integerbox("How many teams?")

#declaration of arrays
names_list = inputNames.split()
names_array = np.array(names_list)

print('There will be :',(len(names_array))/inputNoTeams, 'player/s in each team')
#blank array
jumbled = np.empty(len(names_array), dtype=object)
#random number list
your_list = list(np.random.choice(np.arange(0,len(names_array)), len(names_array), replace=False))
#order the array with strings
for i in range(len(names_array)):
    jumbled[i] = names_list[your_list[i]]
#split the array
newarr = np.array_split(jumbled, inputNoTeams)
#output formatting
for j in range(inputNoTeams):
    print("Team ",j+1," :")
    print(newarr[j])
