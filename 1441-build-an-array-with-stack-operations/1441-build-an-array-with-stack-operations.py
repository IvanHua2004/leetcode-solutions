class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        current = 1
        for i in target:
            while True:
                if current == i:
                    result.append("Push")
                    current += 1
                    break
                result.append("Push")
                result.append("Pop")
                current += 1
        return result
