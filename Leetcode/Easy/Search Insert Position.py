def search_insert(nums, target):
    if target in nums:
        return nums.index(target)

    while True:
        for index, obj in enumerate(nums):
            if target > nums[-1]:
                nums.append(target)
                return nums.index(target)

            elif target < obj:
                nums.insert(index, target)
                return nums.index(target)
        break

print(search_insert([1, 4, 5, 7, 9, 11], 6))