class Solution:

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakDict = {index: num.count(1) for index, num in enumerate(mat)}

        sortedDict = dict(sorted(weakDict.items(), key=lambda item: item[1]))
        answer = []

        for key, value in sortedDict.items():
            answer.append(key)

        return answer[:k]