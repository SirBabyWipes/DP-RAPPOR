
import random
import math



# Reads the csv file and writes the age counts to ageCounts dict
def realFileCounts(fileToRead):
    ageCounts = [0] * 74
    with open(fileToRead, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            ageCounts[int(line)-17] += 1

    return ageCounts

#
def rapporFileCounts(fileToRead, epsilon):
    epsilon = float(epsilon)
    p = (math.e**(epsilon / 2))/(math.e**(epsilon / 2)+ 1)
    q = 1 /(math.e**(epsilon / 2)+1)
    binaryAgeCounts = []
    ageCounts = [0] * 74
    with open(fileToRead, "r", encoding="utf-8") as file:
        next(file)
        for line in file:
            binaryAgeCounts.append(toBinaryVector(int(line)))
        for i in range(len(binaryAgeCounts)):
            encode(binaryAgeCounts[i], epsilon, p, q)

    for list in binaryAgeCounts:
        for i in range(len(list)):
            if list[i] == 1:
                ageCounts[i] += 1

    n = len(binaryAgeCounts)
    return ageCounts, p, q, n

#
def toBinaryVector(age):
    vector = [0] * 74
    vector[age-17] = 1

    return vector

#
def encode(vec, epsilon, p, q):
 
    for i in range(len(vec)):
        ran = random.random()
        if vec[i] == 0:
            if ran < q:
                vec[i] = 1
        else:
            if ran >= p:
                vec[i] = 0


#
def estimator(rap, p, q, n):
    estimates = []
    for i in rap:
        est = (i - n * q) / (p - q)
        estimates.append(est)
    return estimates  

#
def meanAbsoluteError(trueCounts, estimates):
    total = (sum(abs(t - e) for t, e in zip(trueCounts, estimates))) / len(trueCounts)
    return total



def main():
    epsilon = input("input your epsilon value: ")
    trueCounts = realFileCounts('adult_age_dataset.csv')

    rapCounts, p, q, n = rapporFileCounts('adult_age_dataset.csv', epsilon)
    estimates = estimator(rapCounts, p, q, n)
    #print(estimates) 
    mae = meanAbsoluteError(trueCounts, estimates)



    print(f"MAE for epsilon = {mae}")

main()