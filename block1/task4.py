class Solution:

    def k_weakest_rows(self, mat: List[List[int]], k: int) -> List[int]:
        weak_dict = {index: num.count(1) for index, num in enumerate(mat)}

        sorted_dict = dict(sorted(weak_dict.items(), key=lambda item: item[1]))
        answer = []

        for key, value in sorted_dict.items():
            answer.append(key)

        return answer[:k]
