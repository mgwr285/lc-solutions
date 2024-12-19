class Solution:
    def frequencySort(self, s: str) -> str:
        counter = sorted(Counter(s).items(), key=lambda c: -c[1])
        res = []
        for char, count in counter:
            res.extend([char] * count)
        return "".join(res)
