

class QuestionOfSearching:
    def __inti__(self):
        self.name = "Practice Question for Searching"

        def binarysearch(self, arr, n, k):
            # code here
            st = 0
            ed = n - 1
            mid = 0
            while st <= ed:
                mid = (st + ed) // 2

                if arr[mid] == k:
                    return mid
                elif arr[mid] < k:
                    st = mid + 1

                else:
                    ed = mid - 1


            return -1