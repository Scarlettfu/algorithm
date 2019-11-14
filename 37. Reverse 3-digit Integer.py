class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    Example
    Reverse 123 you will get 321.

    Reverse 900 you will get 9
    """

    def reverseInteger(self, number):
        # write your code here

        firChar = number / 100
        secChar = number % 100 / 10
        thirChar = number % 10 #use this method not "number - firchar - secchar*10", it's waste more time

        return thirChar * 100 + secChar * 10 + firChar
