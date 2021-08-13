#function to return key for any value

def get_key(val):
	for key, value in my_dict.items():
		if val == value:
			return key

	return "key doesn't exist"

# Driver Code

my_dict ={"java":100, "python":112 ,"c":[11,'']}

print(get_key(100))
print(get_key(11))
