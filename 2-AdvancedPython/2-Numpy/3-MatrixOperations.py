import numpy as np
# q1 and q2 are sales of different products in different countries
                # country
q1 = np.array([[200,220,250],  # product A
               [150,180,210],  # product B
               [300,330,360]]) # product C
q2 = np.array([[209,231,259],
               [155,192,222],
               [310,340,375]])

print(q1 + q2) # gives total revenue of each product in different countries

print(q2-q1)  # sales qrowth in q1

print(((q2-q1)* 100)/q1) # sales growth % from Q1

prices = np.array([[10,12,11], # prices of product A in different regions
                   [8,9,10],
                   [15,16,17]])

q1_revenue = q1 * prices
print(q1_revenue)

# there is 20 % discount on products in q1, cal discount value
discount_rev = q1_revenue * 0.2
print(discount_rev)

net_revenue = q1_revenue - discount_rev
print(net_revenue)

# total discount on all products in all regions

print(np.sum(discount_rev))

# dot product

features = np.array([
    [2000,3], # house 1
    [1800,2]  # house 2
])

weights = np.array([150,50000])

print(np.dot(features,weights))

# cross product

c = np.array([1,2,3])
d = np.array([4,5,6])
print(np.cross(c,d))



