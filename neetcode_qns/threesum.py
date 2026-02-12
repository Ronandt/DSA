class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_number = list(sorted(nums))
        tripets = []
        #[-1,0,1,2,3,4] #0 
        print(sorted_number)
        for x in range(len(sorted_number)):
            if x > 0 and sorted_number[x-1] == sorted_number[x]:
                continue

            second_pointer = len(nums) -1
            first_pointer = x + 1
            #cannot overlap with duplicates
            while second_pointer > first_pointer:
                total = sorted_number[x] + sorted_number[second_pointer] + sorted_number[first_pointer]


                if total == 0:
                    tripets.append([sorted_number[x], sorted_number[first_pointer], sorted_number[second_pointer]])
                    


                    while second_pointer > first_pointer and sorted_number[second_pointer] == sorted_number[second_pointer-1]:
                        second_pointer -= 1
                    while second_pointer > first_pointer and sorted_number[first_pointer] == sorted_number[first_pointer +1]:
                        first_pointer +=1 
                    first_pointer += 1
                    second_pointer -= 1
                   
                elif total > 0:
                    second_pointer -=1
                else:
                    first_pointer +=1
        return tripets