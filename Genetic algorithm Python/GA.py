import csv
import random

item = []
utility = []
weight = []
total = []
parent1 = [1,1,1,1,1,1,1,1]
parent2 = [1,0,1,0,1,0,1,0]

with open('beach.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            item.append(row[0])
            utility.append(row[1])
            weight.append(row[2])
            line_count += 1
    
def crossover(p1, p2, r_cross):
    	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()
	# check for recombination
	if random.random()/8*10 < r_cross:
		# select crossover point that is not on the end of the string
		pt = random.randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]



def mutation(p1):
    c1 = p1.copy()
    if random.random() > 0.7:
        pt = random.randint(0, len(p1)-1)
        if c1[pt]==0:
            c1 = p1[:pt] +[1]+ p1[pt+1:]
        if c1[pt]==1:
            c1 = p1[:pt] +[0]+ p1[pt+1:] 
    return c1           
def calculateUtility(p):
    uti = 0
    for i in range(0,8):
        uti += int(utility[i+1])*int(p[i])
    return uti    
def calculateWeight(p):
    wei = 0
    for i in range(0,8):
        wei += int(weight[i+1])*int(p[i])
    return wei
        
def multi(p1, p2):
    c1 = []
    c2 = []
    for i in range(0,8):
        if i<2:
            c1.append(p2[i])
            c2.append(p1[i])
        elif i<5:
            c1.append(p1[i])
            c2.append(p2[i])  
        else:
            c1.append(p2[i])
            c2.append(p1[i]) 
    return [c1,c2]                      


resultUti = []
resultPar = []
for i in range(0,100):
    [parent1,parent2] = crossover(parent1,parent2,8)
    parent1 = mutation(parent1)
    parent2 = mutation(parent2)
    if calculateWeight(parent1)<=15:
        ut = calculateUtility(parent1)
        resultUti.append(ut)
        resultPar.append(parent1)
    if calculateWeight(parent2)<=15:
        ut = calculateUtility(parent2)
        resultUti.append(ut)
        resultPar.append(parent2)    
    if i in [10,20,30]:
        ma = max(resultUti)
        mi = min(resultUti)
        ma_index = resultUti.index(ma);
        mi_index = resultUti.index(mi);
        if i==10:
            print("Runs: 10,Epochs: 100 Population size: 10  crossover:one-point") 
        if i==20:
            print("Runs: 20,Epochs: 100 Population size: 20  crossover:one-point") 
        if i==30:
            print("Runs: 30,Epochs: 100 Population size: 30  crossover:one-point") 
        str1 = "Min "+str(mi)+"{'items' :"+str(resultPar[mi_index]) +"}"
        str2 = "Max "+str(ma)+"{'items' :"+str(resultPar[ma_index]) +"}" 
        str3 = "average "+str(mi/2+ma/2) 
        print(str1)
        print(str2)
        print(str3)
        
resultUti = []
resultPar = []
parent1 = [1,1,1,1,1,1,1,1]
parent2 = [1,0,1,0,1,0,1,0]
for i in range(0,100):
    [parent1,parent2] = multi(parent1,parent2)
    parent1 = mutation(parent1)
    parent2 = mutation(parent2)
    if calculateWeight(parent1)<=15:
        ut = calculateUtility(parent1)
        resultUti.append(ut)
        resultPar.append(parent1)
    if calculateWeight(parent2)<=15:
        ut = calculateUtility(parent2)
        resultUti.append(ut)
        resultPar.append(parent2)    
    if i in [10,20,30]:
        ma = max(resultUti)
        mi = min(resultUti)
        ma_index = resultUti.index(ma);
        mi_index = resultUti.index(mi);
        if i==10:
            print("Runs: 10,Epochs: 100 Population size: 10  crossover:multi-point") 
        if i==20:
            print("Runs: 20,Epochs: 100 Population size: 20  crossover:multi-point") 
        if i==30:
            print("Runs: 30,Epochs: 100 Population size: 30  crossover:one-point") 
        str1 = "Min "+str(mi)+"{'items' :"+str(resultPar[mi_index]) +"}"
        str2 = "Max "+str(ma)+"{'items' :"+str(resultPar[ma_index]) +"}" 
        str3 = "average "+str(mi/2+ma/2) 
        print(str1)
        print(str2)
        print(str3)        
    
