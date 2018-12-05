def commonCharacterCount(s1, s2):

    dict1 = {}
    dict2 = {}
    common = 0
    
    for letter in s1:
        if dict1.get(letter):
            dict1[letter] += 1
        else:
            dict1[letter] = 1
    
    for letter in s2:
        if dict2.get(letter):
            dict2[letter] += 1
        else:
            dict2[letter] = 1
            
    for key, value in dict1.items():
        if dict2.get(key):
            if value > dict2[key]:
                common += dict2[key]
            elif value <= dict2[key]:
                common += value
                
    return common