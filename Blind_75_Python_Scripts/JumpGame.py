def jump(nums):
   goalpost = len(nums) - 1

   for i in range(len(nums)-1, -1, -1):
       if i + nums[i] >= goalpost:
           goalpost = i

   return True if goalpost == 0 else False


jumps = [2, 3, 1, 1, 4]
