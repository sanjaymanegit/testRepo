my_str = "hello world"
my_str_as_bytes = str.encode(my_str)
type(my_str_as_bytes) # ensure it is byte representation
print("my_str_as_bytes :"+str(type(my_str_as_bytes)))
my_decoded_str = my_str_as_bytes.decode()
type(my_decoded_str) # ensure it is string representation
print("my_decoded_str:"+str(type(my_decoded_str)))