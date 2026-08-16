s = "anagram"
t = "nagaram"
def isAnagram(s,t):
    if sorted(s.lower())==sorted(t.lower()):
        return True
    else:
        return False
print(isAnagram(s,t))