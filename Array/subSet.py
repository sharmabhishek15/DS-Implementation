def subSet(arr, i, temp, ans):
    if i == len(arr):
        print(ans)
    else:
        subSet(arr[1:],i+1,temp,ans[0])




if __name__ == '__main__':
    arr = [1,2,3]
    temp = []
    ans = []
    subSet(arr,0,temp,ans)
