print("Hello")

def has_lucky_number(nums):
    return True if any([num%7 == 0 for num in nums]) else False
        

l = [ 1  , 6 , 78 , 89 , 49 , 50]
print(has_lucky_number(l))
