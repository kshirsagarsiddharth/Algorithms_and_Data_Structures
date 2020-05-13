from collections import Counter

input =['john','johnny','jackie','johnny','john','jackie','jamie','jamie', 
'john','johnny','jamie','johnny','john'] 
def winner(input):
    votes = Counter(input)
    dictonary = dict()
    for number in votes.values():
        dictonary[number] = []

    for (key,value) in votes.items():
        dictonary[value].append(key)

    max_value = sorted(dictonary.keys(),reverse = True)[0]

    if len(dictonary[max_value]) > 0:
        print(sorted(dictonary[max_value])[0])
    else:
        print(dictonary[max_value][0])

# %%
votes = Counter(input)
max_val = max(votes.values())
[i for i in votes.keys() if votes[i] == max_val][0]