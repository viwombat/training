class Solution:

    def k_weakest_rows(self, mat: List[List[int]], k: int) -> List[int]:
        weak_list = {index: num.count(1) for index, num in enumerate(mat)}
        weak_list.sort(key=lambda x: x[1])

        answer = [index for index, num in weak_list]

        return answer[:k]
