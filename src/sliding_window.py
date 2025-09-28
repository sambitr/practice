def sliding_window(arr, k):
    max_result = 0
    len_arr = len(arr)
    for i in range(len_arr -k + 1):
        tmp_max_result = sum(arr[i:i+k])
        if tmp_max_result > max_result:
            max_result = tmp_max_result
    
    return  max_result
            


# sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3)  # Expected output: [3, 3, 5, 5, 6, 7]
# sliding_window([2,1,5,1,3,2], 3)  # Expected output: [3, 3, 5, 5, 6, 7]
# sliding_window([3, 5, 2, 1, 7], 2)