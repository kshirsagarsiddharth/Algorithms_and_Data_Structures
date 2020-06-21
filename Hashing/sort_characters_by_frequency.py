def frequencySort(s: str) -> str:
    freq = {}
    for val in s:
        freq[val] = freq.ger(val,0) + 1
    
    freq_sorted = sorted(freq.items(),key = lambda x :x[1],reverse = True)
    return ''.join(i[0] * i[1] for i in freq_sorted)
