class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        res = []
        for w in words:
            top = 0
            mid = 0
            bot = 0
            put = True
            for l in w:
                if l.lower() in first:
                    top = 1
                elif l.lower() in second:
                    mid = 1
                elif l.lower() in third:
                    bot = 1
                
                if (top and mid) or (bot and mid) or (top and bot):
                    put = False
            if put == True:
                res.append(w)
        return res
