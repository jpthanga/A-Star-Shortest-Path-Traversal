#Jeshuran Thangaraj
#jpthanga@iu.edu
import yaml 
import math
import operator
import sys
from sys import argv

x=0
y=1
doc = open(argv[1],"r")
test = yaml.load(doc)
s = test.get('start')
e = test.get('end')
cityList = test.get('cities')
highways = test.get('highways')
closed = []

#calculate cost
def findCost(fromCity , toCity):
    cost = math.sqrt(((fromCity[x] - toCity[x])**2) + ((fromCity[y] - toCity[y])**2))
    return cost

#Calculate h(x)
def expectedCost(fromCity):
    toCity=cityList[e]
    cost = math.sqrt(((fromCity[x] - toCity[x])**2) + ((fromCity[y] - toCity[y])**2))
    return cost

#A* search
def search(fringe):
    while(True):
        progress = []
        pick = sorted(fringe.items(), key=operator.itemgetter(1))[0]
        costValue = pick[1]
        currentgh = costValue[0]
        currentg = costValue[2]
        currenth = costValue[1]
        currentPick = pick[0]
        
        #Goal Achieved
        if currentPick == e:
            print(str(currentg))
            return

        
        #get succesors
        for each in highways:
            if currentPick in each:
                if(each[0] == currentPick):
                    if(each[1] not in closed):
                        progress.append(each[1])
                else:
                    if(each[0] not in closed):
                        progress.append(each[0])
        
        #add to fringe
        for each in progress:
            if(cityList[currentPick][y] > cityList[each][y]):
                continue 
            newh = expectedCost(cityList[each])
            cost = currentg + findCost(cityList[currentPick], cityList[each])
            newSum = cost + newh
            #if node already in fringe
            if each in fringe.keys():
                old = fringe[each][2]
                if old > cost:
                    fringe[each] = (newSum,newh,cost)
            else:
                    fringe[each] = (newSum,newh,cost)
        
        #close visited
        del fringe[currentPick]
        closed.append(currentPick)
        progress.clear()
        
        #Goal impossible
        if(len(fringe) == 0):
            print("No Path Found")
            return
    
def main(argv):
    #initial h(x)
    if(cityList[s][y] > cityList[e][y]):
        print("No Path Found")
        return
    exp = expectedCost(cityList[s])
    #create fringe
    fringe = {s: (exp,exp,0)}
    search(fringe)

if __name__ == "__main__":
    main(sys.argv[1:])
