from collections import Counter
def topk_frequentElements(nums: List[int],k: int) -> List[int]:
    c = Counter(nums)
    return sorted(c, key = lambda x: c[x],reverse = True)[:k]