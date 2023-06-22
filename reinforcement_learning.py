import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from collections import Counter
import time

dataset = pd.read_csv('powerball_numbers.csv')
balls = dataset.iloc[:, 1:6].values
powerball = dataset.iloc[:, -1].values

# Pre-process data for algorithm
X_balls = np.zeros((balls.shape[0], 69))
X_powerball = np.zeros((powerball.shape[0], 26))

for i in range(balls.shape[0]):
    for j in balls[i]:
        X_balls[i, j-1] = 1

if i in range(powerball.shape[0]):
    X_powerball[i, powerball[i]-1] = 1

random.seed(0)

# Predict 5 numbers
N = balls.shape[0]
d = 69
num_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
for n in range(N):
    max_random = 0
    num = 0
    for i in range(d):
        random_beta = random.betavariate(numbers_of_rewards_1[i]+1,
                                         numbers_of_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            num = i
            
    num_selected.append(num)
    if X_balls[n, num] == 1:
        numbers_of_rewards_1[num] += 1
    else:
        numbers_of_rewards_0[num] += 1
        
pick_five_balls = [i+1 for i, _ in Counter(num_selected).most_common(5)]

# Predict powerball number
N = powerball.shape[0]
d = 26
num_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
for n in range(N):
    max_random = 0
    num = 0
    for i in range(d):
        random_beta = random.betavariate(numbers_of_rewards_1[i]+1,
                                         numbers_of_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            num = i
            
    num_selected.append(num)
    if X_powerball[n, num] == 1:
        numbers_of_rewards_1[num] += 1
    else:
        numbers_of_rewards_0[num] += 1
        
pick_powerball = [i+1 for i, _ in Counter(num_selected).most_common(1)]

print(""" 

__________                         __________        .__  .__   
\______   \______  _  __ __________\______   \_____  |  | |  |  
 |     ___/  _ \ \/ \/ // __ \_  __ \    |  _/\__  \ |  | |  |  
 |    |  (  <_> )     /\  ___/|  | \/    |   \ / __ \|  |_|  |__
 |____|   \____/ \/\_/  \___  >__|  |______  /(____  /____/____/
                            \/             \/      \/           
         _________      .__                                     
        /   _____/ ____ |__| ____   ____   ____  ____           
        \_____  \_/ ___\|  |/ __ \ /    \_/ ___\/ __ \          
        /        \  \___|  \  ___/|   |  \  \__\  ___/          
       /_______  /\___  >__|\___  >___|  /\___  >___  >         
               \/     \/        \/     \/     \/    \/ 
               
                    Donate cashapp $zlite4         

 """)

print(('Most Used Powerballs: ', sorted(pick_five_balls), pick_powerball))


