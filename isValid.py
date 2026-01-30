def isValid(s):
    l = []
    c_map = {")":"(", "]":"[", "}": "{"}
    for c in s:
        if c in c_map:
            if l and l[-1] == c_map[c]:
                l.pop()
            else:
                return False
        else:
            l.append(c)

    return True if not l else False

s = "([)]"
print(isValid(s))
    