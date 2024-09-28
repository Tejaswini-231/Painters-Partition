                                      ---------------PAINTERS PARTITION-----------------------

---canPaint(boards, n, painters, maxTime):

This function checks if it’s possible to paint all the boards using the given number of painters such that no painter spends 
more than maxTime on their assigned boards.

=>Inputs:

boards: The list of board lengths.
n: The number of boards (length of the boards array).
painters: The number of painters available.
maxTime: The maximum time any painter is allowed to spend painting.

=>Logic:

Start with one painter (count = 1) and let them start painting the boards.
For each board, check if adding that board’s length to the painter’s current workload (timeSpent) would still be within the allowed maxTime.
If not, assign a new painter to start with that board.
If at any point the number of painters exceeds the available number (painters), return False.
If all boards are assigned to the painters within maxTime, return True.

---paintersPartition(boards, n, painters):

This is the main function that uses binary search to find the minimum possible maximum time any painter would need to spend.

=>Inputs:

boards: The list of board lengths.
n: The number of boards.
painters: The number of painters.

=>Logic:
The minimum possible time (low) a painter could take is the length of the longest board (max(boards)), because no painter can paint less than the longest board.
The maximum possible time (high) is the sum of all the board lengths (sum(boards)), as that’s the time one painter would take if they had to paint all the boards alone.
Perform binary search on the range [low, high] to find the smallest mid value (candidate maxTime) such that all painters can paint the boards within that time.
The canPaint function is used to check if it's possible to assign all boards with the current mid time.

low = mid + 1: You do this when mid is too small, and you need to search for a larger time.
high = mid - 1: You do this when mid is valid, but you want to check if a smaller time might also work,
 so you search the smaller half of the range.

Case 1: If the painters can paint all boards within 70 units of time:
You reduce the upper bound because you want to check if a smaller time might still work:
high = mid - 1 = 70 - 1 = 69.
Case 2: If the painters cannot paint all boards within 70 units of time:
You increase the lower bound because you need more time:
low = mid + 1 = 70 + 1 = 71.
This process continues until low exceeds high, meaning you have found the smallest valid time.
