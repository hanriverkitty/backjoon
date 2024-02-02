s = "abc"
t = "ahbgdc"


def isSubsequence(s, t):
    prev = -1
    result = False
    if s == "":
        return True
    for i in range(len(s)):
        result = False
        for j in range(prev + 1, len(t)):
            if s[i] == t[j]:
                prev = j
                result = True
                print(prev)
        if result == False:
            return False
    if result == True:
        return True


isSubsequence(s, t)
