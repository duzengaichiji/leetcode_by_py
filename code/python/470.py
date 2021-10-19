# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = (rand7()-1)*7+rand7()
            if num<=40:
                return 1+num%10
            num = (num-40-1)*7+rand7()
            if num<=60:
                return 1+num%10
            num = (num-60-1)*7+rand7()
            if num<=20:
                return 1+num%10