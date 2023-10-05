class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = {}
        for a in s:
            mp[a] = mp.get(a,0) + 1
        

        size=0
        odd=False
        for letter, freq in mp.items():
            if(freq % 2 == 0):
                size+=freq
            if(freq % 2 != 0):
                size+=freq-1
                odd = True
        
        if(odd):
            return size + 1
        return size
