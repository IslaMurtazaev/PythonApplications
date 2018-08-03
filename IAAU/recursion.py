# “A human is someone whose mother is human”.

# Program by Mitchell Aikens
# No Copyright
# 2010

num = 0

def main():
    counter(num)

def counter(num):
    print(num)
    num += 1
    counter(num)

main()

#====================================================
# Program by Mitchell Aikens
# No copyright
# 2012
def main():
    loopnum = int(input("How many times would you like to loop?\n"))
    counter = 1
    recurr(loopnum,counter)

def recurr(loopnum,counter):
    if loopnum > 0:
        print("This is loop iteration",counter)
        recurr(loopnum - 1,counter + 1)
    else:
        print("The loop is complete.")

main()




# ===================================================
#!/usr/bin/env python
 
def sum(list):
    sum = 0
 
    # Add every number in the list.
    for i in range(0, len(list)):
        sum = sum + list[i]
 
    # Return the sum.
    return sum
 
print(sum([5,7,3,8,10]))

#!/usr/bin/env python
 
def sum(list):
   if len(list) == 1:
        return list[0]
   else:
        return list[0] + sum(list[1:])
 
print(sum([5,7,3,8,10]))


>>> def sum_digits(n):
        """Return the sum of the digits of positive integer n.
       	>>> sum_digits(9)
		9
		>>> sum_digits(18117)
		18
		>>> sum_digits(9437184)
		36
		>>> sum_digits(11408855402054064613470328848384)
		126
        """
        if n < 10:
            return n
        else:
            all_but_last, last = n // 10, n % 10
            return sum_digits(all_but_last) + last



# Write a Python program to calculate the value of 'a' to the power 'b
# (power(3,4) -> 81

# Write a Python program to converting an Integer to a string in any base.

# Write a Python program of recursion list sum.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21