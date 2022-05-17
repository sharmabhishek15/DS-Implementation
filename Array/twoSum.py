###---------------------------------------------------------###

# def subArraySum(arr, n, sum_):
#     """
#     Input: N = 5, S = 12 , A[] = {1,2,3,7,5}, Output: 2 4
#     Explanation: The sum of elements
#     from 2nd position to 4th position
#     is 12.
#     """
#     A = []
#     curr_sum = arr[0]
#     start = 0
#     i = 1
#     while i <= n:
#         while curr_sum > sum_ and start < i - 1:
#             curr_sum = curr_sum - arr[start]
#             start += 1
#         if curr_sum == sum_:
#             A.append(start + 1)
#             A.append(i)
#             return A
#         if i < n:
#             curr_sum = curr_sum + arr[i]
#         i += 1
#     A.append(-1)
#     return A

# def subArraySum(arr, target, n):
#     dp = {}
#     ans = []
#     for i in arr:
#         if target-i not in dp:
#             dp[i] = i
#         else:
#             ans.append((i, target-i))
#     if not ans:
#         ans.append((-1,-1))
#
#     return ans

def twoSum(arr, target, n):
    hashMap = {}

    ans = []

    for i in range(n):
        if arr[i] in hashMap:
            hashMap[arr[i]] += 1
        else:
            hashMap[arr[i]] = 1

        if target - arr[i] not in hashMap:
            continue

        if target - arr[i] == arr[i]:

            # Valid pair will only exist if frequency of arr[i] is greater than 1.
            if hashMap[arr[i]] > 1:
                ans.append([arr[i], arr[i]])

                # Frequency will decrease by 2
                hashMap[arr[i]] -= 2
        else:

            # For a valid pair frequency of arr[i] and target-arr[i] must be greater than 0.
            if hashMap[arr[i]] > 0 and hashMap[target - arr[i]] > 0:
                ans.append([arr[i], target - arr[i]])

                # Frequency will decrease by 1.
                hashMap[arr[i]] -= 1

                hashMap[target - arr[i]] -= 1

    # If no valid pair exists.
    if len(ans) == 0:
        ans.append([-1, -1])

    return ans
arr = [2, 7, 11, 13]
n = 4
sum_ = 9
print(twoSum(arr, sum_, n))

