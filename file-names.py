# Nice, clean solution from Codesignal

def fileNaming(names):
    """You are given an array of desired filenames in the order of their 
    creation. Since two files cannot have equal names, the one which comes 
    later will have an addition to its name in a form of (k), where k is the 
    smallest positive integer such that the obtained name is not used yet.

    Return an array of names that will be given to the files."""

    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names



# My solution - definitely more convoluted

# def check_name(name, names_dict):
    
#     if name in names_dict.keys():
#         num = int(name[-2])
#         new_name = name[:-2] + str(num + 1) + ")"
#         names_dict[name[:-3]] += 1
#         new_name = check_name(new_name, names_dict)
#         return new_name
        
#     else:
#         names_dict[name] = 1
#         return name
    

# def fileNaming(names):
    
#     names_dict = {}

#     for i in range(len(names)):
#         if names[i] in names_dict.keys():
#             num = names_dict[names[i]]
#             new_name = names[i] + "(" + str(num) + ")"
#             names_dict[names[i]] += 1
#             names[i] = check_name(new_name, names_dict)
#         else:
#             names_dict[names[i]] = 1
            
#     return names


# First try - didn't rename some files correctly... added nums instead of inc.

# def check_name(name, names_dict):
#     if name in names_dict.keys():            
#         new_name = name + "(" + str(names_dict[name]) + ")"
#         names_dict[name] += 1
#         new_name = check_name(new_name, names_dict)
#         return new_name
        
#     else:
#         names_dict[name] = 1
#         return name
    

# def fileNaming(names):
    
#     names_dict = {}

#     for i in range(len(names)):
#         names[i] = check_name(names[i], names_dict)
            
#     return names