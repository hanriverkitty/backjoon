class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []
        answer1 = set(nums1)
        answer2 = set(nums2)
        answer1 = list(answer1)
        answer2 = list(answer2)
        index = []
        for i in answer1:
            for j in answer2:
                if i == j:
                    index.append(i)

        for i in index:
            answer1.remove(i)
            answer2.remove(i)

        result.append(answer1)
        result.append(answer2)
        return result

        """
        answer1=set(nums1)
        answer2=set(nums2)
        a=list(answer1-answer2)
        b=list(answer2-answer1)
        result.append(a)
        result.append(b)
        """
