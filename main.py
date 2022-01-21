# Project 2
# Tyler Hardy
# Assuming Debian install..
# Assuming Python3 install..
# Type "python3 main.py" to run this

import random

## Define user object and instantiate a list with given weights
class user:
    def __init__(self, weight):
        self.weight = weight 
users = []
users.append(user(500))
users.append(user(100))
users.append(user(300))
users.append(user(250))
users.append(user(150))
users.append(user(500))            
users.append(user(600))
users.append(user(350))
users.append(user(200))
users.append(user(150))

## Determine direction based on weighted votes then show who won each supermajority vote
def decide_direction(n):
    leftVote = 0
    leftVoters = []
    rightVote = 0
    rightVoters = []
    id = 0
    for user in users:  
       user_decision = random.randint(0,1)
       if (user_decision == 0):
          leftVote = leftVote+user.weight
          leftVoters.append(id)
       if (user_decision == 1):
          rightVote = rightVote+user.weight
          rightVoters.append(id)
       id += 1
    if (leftVote > rightVote):
        print("These voters selected the supermajority in round " + str(n))
        decision = 0
        print(leftVoters)
    if (leftVote < rightVote):
        print("These voters selected the supermajority in round " + str(n))
        decision = 1
        print(rightVoters)
    if (leftVote == rightVote):
        decision = decide_direction(n)
    return decision

## Randomized path traversal of a full binary tree given by root=0, left=n+1, right=n+2
path = [0]
for n in range(0,10):
    last_node = path[len(path)-1]
    decision = decide_direction(n)
    if (decision == 0):
        path.append(last_node*2+1)
    if (decision == 1):
        path.append(last_node*2+2)
    print("They voted to go from node " + str(last_node) + " to node " + str(path[len(path)-1]) + "\n")
print("\n\nBinary node traversal path:")
print(path)
print("\n\n")
