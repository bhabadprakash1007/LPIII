'''class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

def fractional_knapsack(items, max_capacity):
    items.sort(key=lambda item: item.ratio, reverse=True)
    
    total_value = 0
    current_weight = 0
 
    for item in items:
        if current_weight + item.weight <= max_capacity:
            current_weight += item.weight
            total_value += item.profit
        else:
            remaining_capacity = max_capacity - current_weight
            total_value += item.ratio * remaining_capacity
            break
    
    return total_value
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
max_capacity = 50
max_value = fractional_knapsack(items, max_capacity)
print("Maximum value in the knapsack:", max_value)
'''
class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

def fractional_knapsack(items, max_capacity):
    items.sort(key=lambda item: item.ratio, reverse=True)
    total_value = 0

    for item in items:
        if item.weight <= max_capacity:
            max_capacity -= item.weight
            total_value += item.profit
        else:
            total_value += item.ratio * max_capacity
            break
    
    return total_value

# Example usage
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
print("Maximum value in the knapsack:", fractional_knapsack(items, 50))



# class Item:
# This defines a class Item to represent an object with properties such as weight, profit, and profit-to-weight ratio.

# def __init__(self, weight, profit):
# Initializes an Item instance with weight, profit, and calculates the ratio (profit divided by weight).

# self.weight = weight
# Assigns the weight argument to the weight attribute of the item.

# self.profit = profit
# Assigns the profit argument to the profit attribute of the item.

# self.ratio = profit / weight
# Calculates the profit-to-weight ratio and assigns it to the ratio attribute.

# def fractional_knapsack(items, max_capacity):
# Defines the function fractional_knapsack that takes a list of items and a maximum capacity max_capacity as input.

# items.sort(key=lambda item: item.ratio, reverse=True)
# Sorts the list of items in descending order based on their ratio attribute (profit-to-weight ratio). The item with the highest ratio is placed first to maximize value.

# total_value = 0
# Initializes total_value to store the total value accumulated in the knapsack.

# current_weight = 0
# Initializes current_weight to keep track of the total weight added to the knapsack so far.

# for item in items:
# Starts a loop to iterate through the sorted items one by one.

# if current_weight + item.weight <= max_capacity:
# Checks if adding the current item will not exceed the knapsack's max_capacity.

# current_weight += item.weight
# Adds the weight of the current item to current_weight.

# total_value += item.profit
# Adds the profit of the current item to total_value.

# else:
# If adding the full weight of the current item would exceed the capacity, this block is executed.

# remaining_capacity = max_capacity - current_weight
# Calculates how much more weight can be added to the knapsack (remaining_capacity).

# total_value += item.ratio * remaining_capacity
# Adds the proportional value of the remaining capacity from the current item's profit-to-weight ratio.

# break
# Exits the loop as the knapsack is now full.

# return total_value
# Returns the maximum total value that can be accommodated in the knapsack.

# items = [Item(10, 60), Item(20, 100), Item(30, 120)]
# Creates a list of Item objects with specified weights and profits.

# max_capacity = 50
# Sets the maximum capacity of the knapsack to 50 units.

# max_value = fractional_knapsack(items, max_capacity)
# Calls the fractional_knapsack function with the list of items and max_capacity, and stores the result in max_value.

# print("Maximum value in the knapsack:", max_value)
# Prints the maximum value that can be accommodated in the knapsack.