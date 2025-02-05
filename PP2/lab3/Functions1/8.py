def spy_game(nums):
    global x
    x = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            x += 1
        if x == 2 and nums[i] == 7:
            return True
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0])) 