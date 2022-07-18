def sort(nums):
    #print(nums[0])
    #print("lenth of the list:",len(nums)-1)
    count=1
    for i in range(len(nums)-1,0,-1):
        #length of the list,stop 0 ,decrement -1
        print("iteration1:",count)
        for j in  range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                #print(temp)
               # print(temp, end=" ")
                nums[j]=nums[j+1]
                 # print(nums[j])
                nums[j+1]=temp
                print(nums)
        count=count+1


nums=[5,3,8,6,7,2]
sort(nums)
#print(nums)
