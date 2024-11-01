def is_isogram(string):
    s = string.lower()
    seen = set()
    
    for char in s:
        if char in seen:
            return False 
        if char.isalpha():
            seen.add(char)
    
    return True