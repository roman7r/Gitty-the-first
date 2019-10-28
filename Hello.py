class Car:
	# class veriables
	vehicle_type = "suy"
	model = "S90"

	# Constructor method with instance variables brand and cost
	def __init__(self, brand, cost):
		self.brand=brand
		self.cost=cost

	# Method with instance varible followers
	def fan_follow(self, follow):
		print("This user has " + str(follow) + " follow")
	
def main():
	# First object, set up instance varibles of constructor method
	car=Car('Volvo', 9)
	# Print out instance varible brand
	print(car.brand)
	print(car.cost)

	suv=Car('Honda', 5)
	print(suv.brand)
	print(suv.cost)
	# Use set_followers method and pass followers instance varible
	suv.fan_follow(77)
	# Print out class varible animal_type
	print(suv.vehicle_type)

if __name__ == '__main__':
	main()