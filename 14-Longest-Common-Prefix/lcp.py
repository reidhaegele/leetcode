def lcp(strs) -> str:
    length = len(strs)
    result = ""
    if length == 0: return result
    if length == 1: return strs[0]
    
    for i in range(len(strs[0])):
        letter = strs[0][i]
        for s in strs:
            if (i >= len(s)): 
                return result
            if (s[i]!=letter):
                return result
        result += letter
    
    return result
        

if __name__ == '__main__':
    strings = ["flower", "flow", "flight"]
    print(lcp(strings))