class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0

        while(num):
            if num%2 != 0:
                count += 1
                num = num - 1
            if num>0:
                num = num//2
                count += 1

        return(count)
