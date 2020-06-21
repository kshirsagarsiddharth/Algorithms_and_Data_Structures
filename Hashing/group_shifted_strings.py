from collections import defaultdict

def genKey(word : str) -> str:
    return ':'.join([str((ord(word[i]) - ord(word[i - 1])) % 26) for i in range(1,len(word))])

def groupStrings(strings: List[str]) -> List[List[str]]:
    dd = defaultdict(list)
    for s in strings:
        dd[genKey(s)].append(s)
    
    return [sorted(l) for l in dd.values()]
