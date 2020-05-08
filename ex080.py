nums = []

for c in range(0, 5):
    n = int(input('Digite uma valor: '))

    if c == 0 or n > nums[len(nums)-1]:
        nums.append(n)
    else:
        pos = 0
        while pos < len(nums):
            if n <= nums[pos]:
                nums.insert(pos, n)
                break
            pos += 1
print(nums)

    