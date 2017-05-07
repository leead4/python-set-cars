
# Create an empty set named showroom.
showroom = set()

# Add four of your favorite car model names to the set.
showroom.add("accord")
showroom.add("model_T")
showroom.add("carraige")
showroom.add("horse")

# Print the length of your set.
print(showroom)

# Pick one of the items in your show room and add it to the set again.
showroom.add("horse")

# Print your showroom. Notice how there's still only one instance of that model in there.
print("showroom", showroom)

# b = set()
b = ["pants", "panda"]

# Using update(), add two more car models to your showroom with another set.
showroom.update(b)

print("showroom updated", showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("panda")

print("showroom discard", showroom)


# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old 
# cars has approached you about buying the entire inventory. In the new set, add some different cars, 
# but also add a few that are the same as in the showroom set.
junkyard = ["cat-sleigh", "chariots", "panda", "pants", "nissan", "plane"]

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
inter_stuff = showroom.intersection(junkyard)
new = showroom.union(junkyard)	

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.

print("combined", new)

new.discard("nissan")

print(new)



