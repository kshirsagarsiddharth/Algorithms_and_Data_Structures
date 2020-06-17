def letter_combinations(digits):
    dic = {"2":["a","b","c"],
               "3":["d","e","f"],
               "4":["g","h","i"],
               "5":["j","k","l"],
               "6":["m","n","o"],
               "7":["p","q","r","s"],
               "8":["t","u","v"],
               "9":["w","x","y","z"]
              }
    output = []
    def helper(combination,next_digit):
        if not next_digit:
            output.append(combination)
        else:
            for letter in dic[next_digit[0]]:
                helper(combination + letter,next_digit[1:])
    
    if digits:
        helper("",digits)
        return output
    else:
        return []
        