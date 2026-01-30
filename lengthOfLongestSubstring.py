def lengthOfLongestSubstring(s):
        maxi = 0
        hs = set()
        l = 0
        j = 0
        while j != len(s):
            if s[j] not in hs:
                hs.add(s[j])
                j+=1
                l+=1
                print(l)
                maxi = max(maxi, l)
            else:
                hs.remove(s[j - l])
                print(hs)
                l -=1
                
        return maxi
    

print(lengthOfLongestSubstring("abcabcbb"))


  

