def canPaint(boards, n, painters, maxTime):
    count = 1  # Start with 1 painter
    timeSpent = 0  # Track the time the current painter has spent

    for i in range(n):
        if timeSpent + boards[i] <= maxTime:
            timeSpent += boards[i]  # Painter can paint this board within maxTime
        else:
            count += 1  # Assign the board to a new painter
            timeSpent = boards[i]  # Start this painter's time with the current board
        if count > painters:
            return False  # More painters needed than available
    return True  # All painters can paint within the maxTime


def paintersPartition(boards, n, painters):
    low, high = max(boards), sum(boards)  # Min and max possible times
    res = high

    while low <= high:
        mid = (low + high) // 2  # Try the midpoint time as the candidate maxTime
        if canPaint(boards, n, painters, mid):
            res = mid  # Update result if it's possible to paint within mid time
            high = mid - 1  # Try for smaller maxTime
        else:
            low = mid + 1  # Try for larger maxTime

    return res
