**Part 6: Creating Our Own Problem**

*Mastering Check Digits:*

You meet a girl at the bar and ask for her number. The girl, wanting to check your commitment towards actually getting to know her gives you the first NINE letters of her phone number:  
774-097-683\_  
She tells you that her last digit is a check digit for the rest of the numbers and follows the following criteria:

- Numbering the numbers from right to left, each odd digit is doubled and then added by 1  
- Numbering the numbers from right to left, each even digit is added by 3  
- If the new numbers have two digits \- the new number is the sum of both digits.  
- The check digit is found by alternating plus and minus signs going from right to left starting first with a plus (+) sign  
- When a value has been reached, take the absolute value of the digit and report the number in terms of mod(10)

She asks you to create a function in python that allows you to find the check digit of any 9-digit phone number sequence abiding by these rules.

She says you can check that the function works by finding the check digit of her phone number she already gave you?

Can you find the check digit to her phone number and find her true phone number? Please write a function that returns her true phone number.

**Goals for this problem:**

This problem is meant to assess students' understanding of creating functions, finding the check digit of a sequence of numbers, applying arithmetic rules inside of a function, properly utilizing if/else statements, and eventually apply their knowledge of modular arithmetic. Assessing their understanding of creating a function is explained through the creation of a check\_digit function. Finding the check digit of a sequence of numbers is explored by posing a problem that they need to find the 10th digit of a phone number. Applying arithmetic rules inside of a function is addressed by creating a function that follows all of the rules that the check digit outlines in the girl’s original statement. Using if/else statements applies because in order to code the function they need to use if/else statements for the two digit numbers. Finally, applying their knowledge of modular arithmetic is addressed by following  all of the rules they must find the remainder of their value divided by 10 after their value is absolute valued. Students will be challenged with making sure the syntax of their function is sound and to take the function one rule at a time, however they will learn how to structure functions properly by solving this problem. 