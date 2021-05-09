def removeDuplicates():
    nums = [1, 1, 1, 2]
    # nums.sort()
    print(nums)
    for i in nums:
        if i+1 == i:
            nums.remove(i)
    print(nums)
