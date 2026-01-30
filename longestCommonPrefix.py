def longestCommonPrefix(strs):  
   min_str_len = len(strs[0])
   j = 0
   for i in strs:
      if len(i) < min_str_len:
         min_str_len = len(i)

   while j < min_str_len:
      for k in strs: 
         if k[j] != strs[0][j]:
            return k[0:j]     
      j+=1
   return strs[0][:j]
    
   
                
         
print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["dog","racecar","car"]))
