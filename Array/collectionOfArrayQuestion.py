from math import inf


class QuestionOfArray:
    def __init__(self):
        self.name = "Array Practice Question"

    def leader(self, A, N):
        """
        Input:
        n = 6
        A[] = {16,17,4,3,5,2}
        Output: 17 5 2
        Explanation: The first leader is 17
        as it is greater than all the elements
        to its right.  Similarly, the next
        leader is 5. The right most element
        is always a leader so it is also
        included.
        """
        # Code here [1,2,3,4,0] => [0,4,3,2,1]
        h = -inf
        A = A[::-1]
        op = []
        for i in A:
            if i >= h:
                op.append(i)
                h = i
        op = op[::-1]
        return op

    def equilibriumPoint(self, A, N):
        """Input:
        n = 5
        A[] = {1,3,5,2,2}
        Output: 3
        Explanation: For second test case
        equilibrium point is at position 3
        as elements before it (1+3) =
        elements after it (2+2).
        """
        # Your code here
        sum_ = sum(A)
        curr_sum = 0
        for i in range(N):
            curr_sum += A[i]

            if sum_ - A[i] == curr_sum - A[i]:
                return i + 1
            else:
                sum_ -= A[i]
        return -1

    def subArraySum(self, arr, n, sum_):
        """
        Input: N = 5, S = 12 , A[] = {1,2,3,7,5}, Output: 2 4
        Explanation: The sum of elements
        from 2nd position to 4th position
        is 12.
        """
        A = []
        curr_sum = arr[0]
        start = 0
        i = 1
        while i <= n:
            while curr_sum > sum_ and start < i - 1:
                curr_sum = curr_sum - arr[start]
                start += 1
            if curr_sum == sum_:
                A.append(start + 1)
                A.append(i)
                return A
            if i < n:
                curr_sum = curr_sum + arr[i]
            i += 1
        A.append(-1)
        return A


    def sort012(self, arr, n):
        """
        Input:
        N = 5
        arr[]= {0 2 1 2 0}
        Output:
        0 0 1 2 2
        Explanation:
        0s 1s and 2s are segregated
        into ascending order.
        """
        # code here
        low = 0
        mid = 0
        high = n - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            else:
                mid += 1
        return arr


    def rotateArr(self,A,D,N):
        #Your code here
        A[:]=A[D:]+A[:D]
        return A

    def majorityElement(self, A, N):
        # Your code here
        result = {}
        for i in A:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        # print(result)

        for i in result:
            if result[i] > N / 2:
                return i
        return -1


    def increment(self, arr, N):
        # code here
        carry = 0
        arr = arr[::-1]
        for i in range(0,len(arr)):
            if arr[i] < 9:
                arr[i] += 1
                carry = 0
                return arr[::-1]
            elif arr[i] == 9:
                arr[i] = 0
                carry = 1
        if carry ==1:
            arr = arr + [1]
        return arr[::-1]

    def rearrange(self, arr, n):
        # code here
        # code here
        pos = []
        neg = []
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        arr = []
        temp = 0
        while (len(pos) > 0) or (len(neg) > 0):
            if temp == 0:
                temp = 1
                if pos:
                    arr.append(pos.pop(0))
                else:
                    arr = arr + neg
                    break
            else:
                temp = 0
                if neg:
                    arr.append(neg.pop(0))
                else:
                    arr = arr + pos
                    break
        return arr

    def productExceptSelf(self, nums, n):
        """
        Input:
        n = 5
        nums[] = {10, 3, 5, 6, 2}
        Output:
        180 600 360 300 900
        Explanation:
        For i=0, P[i] = 3*5*6*2 = 180.
        For i=1, P[i] = 10*5*6*2 = 600.
        For i=2, P[i] = 10*3*6*2 = 360.
        For i=3, P[i] = 10*3*5*2 = 300.
        For i=4, P[i] = 10*3*5*6 = 900.
        """
        # code here
        sum_ = 1
        i = 0
        flag = 0
        prod_list = [0] * n
        while i < n:
            if nums[i] != 0:
                sum_ = sum_ * nums[i]
            else:
                flag = flag + 1

            i += 1
        for i in range(n):
            if flag > 1:
                prod_list[i] = 0
            elif flag == 1 and nums[i] != 0:
                prod_list[i] = 0
            elif flag == 0:
                prod_list[i] = sum_ // nums[i]
            else:
                # flag == 1 and nums[i] == 0
                prod_list[i] = sum_

        return prod_list

    def stockBuySell(self, A, n):
        # code here
        buy_stock = 0
        max_profit = 0

        for price in A:
            buy_stock = min(buy_stock, price)
            max_profit = max(max_profit, price - buy_stock)
        if max_profit > 0:
            return 1
        else:
            return 0
