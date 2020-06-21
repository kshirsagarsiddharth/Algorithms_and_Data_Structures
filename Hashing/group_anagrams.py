from collections import defaultdict
def groupAnagrams(strs : List[str]) -> List[List[str]]:
    dd = defaultdict(list)
    strs2 = ["".join(sorted(val)) for val in strs]
    for i,val in enumerate(strs2):
        dd[val].append(strs[i])
    return list(dd.values())


def group_anagrams(strs: List[str]) -> List[List[str]]:
    dd = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(s) - ord("a")] += 1
        dd[tuple(count)].append(s)
    return dd.values()