def sqrt(number):
    """
    Calculate the floored square root of a number
    Run time complexity O(logN)

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number == 0 or number == 1) :
        return number

    start = 1
    end = number
    while start <= end:
        mid = (end + start) // 2
        if mid*mid == number:
            return mid
        if mid*mid < number:
            start = mid + 1
        else:
            end = mid - 1

    return end

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (100 == sqrt(10000)) else "Fail")
# COmp
