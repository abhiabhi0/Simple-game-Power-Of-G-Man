# distance (east or west) with respect to current position on x-axis
def horizontal_direction_wrt_x(src_x, dest_x, curr_direction):
	if (src_x == dest_x):
		return curr_direction
	elif (src_x < dest_x):
		return "E"
	return "W"

# istance (north or south) with respect to current position on y-axis
def same_vertical_direction_wrt_y(src_y, dest_y, curr_direction):
	if (src_y == dest_y):
		return curr_direction
	elif (src_y < dest_y):
		return "N"
	return "S"

def calculate_turns(src_x, src_y, curr_direction, dest_x, dest_y):
	turns = 0

	horizontal_dir = horizontal_direction_wrt_x(src_x, dest_x, curr_direction)
	vertical_dir = same_vertical_direction_wrt_y(dest_x, dest_y, curr_direction)

	if (curr_direction != horizontal_dir):
		turns += 1

	if (curr_direction != vertical_dir):  
		turns += 1

	return turns

def calculate_distance(src_x, src_y, dest_x, dest_y):
	x_dist = abs(src_x - dest_x)
	y_dist = abs(src_y - dest_y)

	return x_dist + y_dist

def calculate_power(src_x, src_y, curr_direction, dest_x, dest_y):
	intial_power = 200
	
	num_turns = calculate_turns(src_x, src_y, curr_direction, dest_x, dest_y)

	min_dist_travelled = calculate_distance(src_x, src_y, dest_x, dest_y)

	power = min_dist_travelled * 10 + num_turns * 5

	return intial_power - power 






