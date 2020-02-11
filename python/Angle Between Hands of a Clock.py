class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle = abs((hour*30 + minutes*0.5) - (minutes*6))

        return(min(360-angle,angle))
        
