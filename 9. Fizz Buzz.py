class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    '''
    Given number n. Print number from 1 to n. But:
    when number is divided by 3, print "fizz".
    when number is divided by 5, print "buzz".
    when number is divided by both 3 and 5, print "fizz buzz".
    '''
    def fizzBuzz(self, n):
        # write your code here
        result = []
        for i in range(1, n + 1):   #'remember: 1: n+1'

            if i % 3 == 0 and i % 5 == 0:
                result.append("fizz buzz")
            elif i % 3 == 0:
                result.append("fizz")
            elif i % 5 == 0:
                result.append("buzz")
            else:
                result.append(str(i))   #" note: str()"

        #test 2019/11/13

        return result