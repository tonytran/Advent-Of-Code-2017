 
def matches(string, i, j):
	return string[i] == string[j]

def sum_matches_half(string):
	max_length_of_orig_list = len(string)
	half = max_length_of_orig_list//2
	i = 0
	j = 0
	_sum = 0
	while(i < max_length_of_orig_list):


		_sum += int(string[j])
		if not matches(string, j, (j+half) % max_length_of_orig_list):
			_sum-=int(string[j])
		j+=1
		i+=1

	return _sum
def sum_matches_next(string):


	max_length_of_orig_list = len(string)
	half = max_length_of_orig_list//2
	i = 0
	j = 0
	_sum = 0
	while(i < max_length_of_orig_list):
		_sum += int(string[j])
		if not matches(string, j, (j+1) % max_length_of_orig_list):
			_sum-=int(string[j])
		j+=1
		i+=1

	return _sum
def main():

	assert sum_matches_next('1122') == 3
	assert sum_matches_next('1111') == 4
	assert sum_matches_next('1234') == 0
	assert sum_matches_next('91212129') == 9

	assert sum_matches_half('1212') == 6
	assert sum_matches_half('1221') == 0
	assert sum_matches_half('123425') == 4
	assert sum_matches_half('123123') == 12
	assert sum_matches_half('12131415') == 4

main()
