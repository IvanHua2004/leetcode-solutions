class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashS = {}
        hashT = {}

        for i in range(len(t)):
            if i < len(t)-1:
                if s[i] not in hashS:
                    hashS[s[i]] = 1
                else:
                    hashS[s[i]] += 1
            if t[i] not in hashT:
                hashT[t[i]] = 1
            else:
                hashT[t[i]] += 1

        for key, value in hashT.items():
            if value != hashS.get(key):
                return key
        