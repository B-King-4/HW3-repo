**Part 5: Creating A Problem:**

*Given that I struggled on generating code for Part 4 of this assignment, I am going to make a similar problem to Part 4 but using different formulas.*

*Multi-Step Calculations and Sub-Functions:*

Counting the Number of Bones From the Animals on a Farm:

Farmer McDonald’s pasture has a fluctuating amount of animals that come into his fields every day. Farmer McDonald has a deal with an artist who makes sculptures out of the animal bones he finds on his farm. When McDonald processes his animals, he gives the bones to the sculptor, who in turn can make the following sculptures from the bones:

For 100 bones, he can create a bone turtle  
For 250 bones, he can create a bone bird  
For 600 bones, he can create a bone butterfly  
For 1500 bones, he can create a bone whale

McDonald has the following animals on his farm, of which the total number of bones they have is given:

Chicken: 120 bones  
Pig: 223 bones  
Cow: 208 bones  
Goat: 189 bones

Write code that can do the following: 

1\. Prompt the user for the amount of each animal that is in the pasture.   
2\. Validate the input to make sure it is not unreasonable.   
3\. Creates a function that totals the amount of bones found on the farm among the animals in the pasture.   
4\. Prints out statements stating how many of each bone sculpture McDonald can trade for and how many bones are left over.  
5\. Challenge: The sculptor can also make his famous ARRAY of sculptures, which includes 4 turtles, 3 birds, 2 butterflies, and a whale. How many ARRAYs can he create given the inputs and how many bones will be left over?

**Goals For this Problem:**

	This problem is meant to assess a coder’s ability to apply multi-step calculations and sub-functions all with respect to python style. The first thing we are proposing a user to do is to check their understanding of creating functions, which is covered by creating a total\_bones() function. Then we are assessing student’s ability to compute multi-step calculations by creating constants for each animal’s bone quantity, multiplying them to the total amount of that animal on that pasture, and then totaling them. We are also continuing this assessment by dividing the total bone amounts by each of the bone amounts required to make the sculptures and the arrays. We will also be testing student’s ability to use subfunctions that are not formal functions by conducting operations based on the prompt steps, which may include setting variables equal to an operation being done on another variable. We are also testing conditionals and ability to validate inputs by the if/else statements validating the total number of animals so there is not an egregious amount of animals on the pasture. We are also assessing their knowledge of python style to see if they follow docstring → constants → functions → driver code format. The hardest part for a student to accomplish will definitely be following the style format, but by styling their code correctly, they will be equipped to organize their code more cleanly in the future   
