#Question 1

# In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.

# To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. 
# You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

# So: what's the product of the following two 64-digit numbers?

x = 3141592653589793238462643383279502884197169399375105820974944592

y= 2718281828459045235360287471352662497757247093699959574966967627

# [TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. 
# Then post your best test cases to the discussion forums to help your fellow students!]

# [Food for thought: the number of digits in each input number is a power of 2.  
# Does this make your life easier?  Does it depend on which algorithm you're implementing?]
def karatsuba(x,y):
  # define a base case
    if len(str(x))==1 or len(str(y))==1:
        return x*y
    else:
      # calculate number of digits and the midpoint
        n = max(len(str(x)),len(str(y)))
        midn = n//2
        
       # split both x and y into halves (a,b) (c,d)
        a = x // 10**(midn)
        b = x % 10**(midn)
        c = y // 10**(midn)
        d = y % 10**(midn)
        
        # create products per karatsuba algorithm
        z0 = karatsuba(b,d)
        z1 = karatsuba((a+b), (c+d))
        z2 = karatsuba(a,c)

        # put products together
        product = (z2 * 10**(2*midn)) + ((z1 - z2 - z0) * 10**(midn)) + (z0)
        return product

    
karatsuba(x,y)
