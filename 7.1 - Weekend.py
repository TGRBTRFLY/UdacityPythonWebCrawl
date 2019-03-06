# Define a procedure, weekend, which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    return day in ('Saturday', 'Sunday')
	
# OR

def weekend(day):
   
    if day.capitalize() == 'Saturday' or day.capitalize() == 'Sunday': 
		return True
    else:
		return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False

