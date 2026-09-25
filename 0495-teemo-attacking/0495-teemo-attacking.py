class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        timer = duration
        for i in range(len(timeSeries)-2, -1, -1):
            difference = timeSeries[i+1] - timeSeries[i]
            timer += duration if difference > duration else difference
        return timer
