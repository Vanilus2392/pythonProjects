def longest_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]
    
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
   

strings = ["flower", "flow", "float"]
print("Longest common prefix:", longest_prefix(strings))