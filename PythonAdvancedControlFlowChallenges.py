def in_range(num,lower, upper) : 
    if (num >= lower) and (num <= upper) : 
        return True
    else : 
        return False

def same_name(your_name, my_name):
    if (your_name == my_name) : 
        return True
    else :
        return False

def always_false(num):
    if (num >= 0) or (num <=0) : 
        return False
    else : 
        return False

def movie_review(rating) : 
    if (rating <= 5) : 
        return "Avoid at all Costs!."
    elif (rating <= 8) and (rating >= 6) : 
        return "This one was fun."
    elif (rating >= 9) : 
        return "Outstanding"

def max_num(num1, num2, num3) : 
    if (num1 > num2) and (num1 > num3) :  
         return num1
    elif (num2 > num3)  and (num2 > num1): 
         return num2
    elif (num3 > num1) and (num3 > num2) : 
        return num3
    else : 
        return "It's a tie!"
