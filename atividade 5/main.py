def max_CrossSum(arr, low, mid, high):
    sm = 0
    left_sum = -10000
 
    for i in range(mid, low-1, -1):
        sm = sm + arr[i]
 
        if (sm > left_sum):
            left_sum = sm
    sm = 0
    right_sum = -1000
    for i in range(mid, high + 1):
        sm = sm + arr[i]
 
        if (sm > right_sum):
            right_sum = sm

    return max(left_sum + right_sum - arr[mid], left_sum, right_sum)

def max_SubArrSum(arr, low, high):
    if (low > high):
        return -10000
    if (low == high):
        return arr[low]
 
    mid = (low + high) // 2
 
    return max(max_SubArrSum(arr, low, mid-1),
               max_SubArrSum(arr, mid+1, high),
               max_CrossSum(arr, low, mid, high))

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
n = len(arr)
 
max_sum = max_SubArrSum(arr, 0, n-1)
print("Maximum adjacent sum ", max_sum)