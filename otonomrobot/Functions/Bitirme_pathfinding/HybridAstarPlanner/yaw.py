
def find_yaw_intervals(yaw_values):
    increasing_intervals = []
    decreasing_intervals = []
    constant_intervals = []
    
    if len(yaw_values) < 2:
        return []

    # 1 for increasing, -1 for decreasing, 0 for constant
    get_direction = lambda a, b: 1 if b > a else -1 if b < a else 0

    intervals = []
    start_index = 0
    current_direction = get_direction(yaw_values[0], yaw_values[1])

    for i in range(2, len(yaw_values)):
        new_direction = get_direction(yaw_values[i - 1], yaw_values[i])
        if new_direction != current_direction:
            intervals.append((start_index, i - 1, current_direction))
            start_index = i - 1
            current_direction = new_direction

    intervals.append((start_index, len(yaw_values) - 1, current_direction))

    """for start, end, direction in intervals:
        if direction == 1:
            increasing_intervals.append((start, end))
        elif direction == -1:
            decreasing_intervals.append((start, end))
        else:
            constant_intervals.append((start, end))"""

    return intervals


    

    
    



