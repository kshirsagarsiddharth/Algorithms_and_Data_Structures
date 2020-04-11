def find_duplicate(string):
    stack = []
    dup = False
    for ch in string:
        if stack and (ch is not stack[-1]) and dup:
            stack.pop()
        if stack and ch is stack[-1]:
            dup = True
        else:
            stack.append(ch)
    if dup:
        stack.pop()

def find_duplicates_using_stacks(string):
    stack = []
    dup = False
    for character in string:
        if stack and (character is not stack[-1]) and dup:
            stack.pop()
        if stack and character is stack[-1]:
            dup = True
        else:
            stack.append(character)
    if dup:
        stack.pop()

        