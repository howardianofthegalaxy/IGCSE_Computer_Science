restaurant_name = input("enter your restaurant name:")
print(restaurant_name)
restaurant_name_length = len(restaurant_name)
print(restaurant_name_length)
if(restaurant_name_length == 0):
    print("YOu cannot enter an empty name")
elif(restaurant_name_length < 5):
    print("name must be more than five letters")
elif(restaurant_name_length > 25):
    print("name must be less than 25 characters")
elif(restaurant_name_length > 5 and restaurant_name_length <25 ):
    print("now your restaurant name is")
    print(restaurant_name) 