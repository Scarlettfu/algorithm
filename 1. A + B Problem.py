class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b

    "&" 与运算： &1 取二进制最后一位数字
    "|" 或运算： |：相当于加运算
    "<<" 左移位： 1000  << 2： 0000
    ">>" 右移     1000 >> 2: 0010

    本题目涉及到： a, b, carry(进位)， 一共有8种可能， 通过判断语句实现
    Note: 重点在于， 处理完所有数据后， 最后的进位符处理

    100:    00000000 00000000 00000000 01100100
    -100:   11111111 11111111 11111111 10011100
    所以当有负数的情况， flag一定为0，不用考虑进位
    """

    def aplusb(self, a, b):
        # write your code here
        sum = 0
        carry = 0
        flag = 0

        for i in range(32):

            if a == 0 and b == 0:
                flag = i
                break
            else:

                a1 = a & 1
                b1 = b & 1
                val = 0

                if a1 == 0 and b1 == 0 and carry == 0:

                    val = 0
                    carry = 0
                elif a1 == 1 and b1 == 1 and carry == 1:

                    val = 1
                    carry = 1
                elif (a1 == 0 and carry == 0) or (b1 == 0 and carry == 0) or (a1 == 0 and b1 == 0):

                    val = 1
                    carry = 0
                else:
                    val = 0
                    carry = 1

                sum |= (val << i)
                a >>= 1
                b >>= 1

            if flag != 0 and carry != 0:

                #very important, when there is '-', flag will be '0', and do not need to think about 'carry'

                sum = sum | (carry << flag)

        return sum


