class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        a = arr[:k]
        s = sum(a)

        if s/k >= threshold:
            count+=1

        for i in range(k,len(arr)):
            item = a[0]
            del a[0]
            a.append(arr[i])
            s += arr[i]
            s -= item
            if s/k >= threshold:
                count += 1
        return(count)
