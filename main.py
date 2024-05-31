def problem1(arr,target):
    for i,v in enumerate(arr):
        for j,w in enumerate(arr):
            if v+w == target:
                return [i,j]
nums = [2,7,11,15]
target = 9
# print(problem1(nums,target))

def problem2(x:int)-> str:
    to_str = str(x)
    return to_str == to_str[::-1]

# print(problem2(121))


def roman_int(s:str)->int:
    keys = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    r = 0

    for i,v in enumerate(s):
        roman_special_rules = v in keys and i+1 < len(s) and s[i+1] in keys
        if not roman_special_rules:
            r += keys[v]
            continue
        n = keys[s[i+1]]
        g = keys[v]
        r = r - g if g<n else r + g
    return r
        
        
        
print(roman_int('MCMXCIV'))
print(roman_int('IV'))
