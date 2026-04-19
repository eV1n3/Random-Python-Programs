weight = 0
ground_transportation = False
premium_transportation = False
drone_transportation = False

#Ground Shipping
if weight > 10.0:
  ground_shipping_cost = 20 + weight * 4.75
elif weight > 6.0:
  ground_shipping_cost = 20 + weight * 4.00
elif weight > 2.0:
  ground_shipping_cost = 20 + weight * 3.00
else:
  ground_shipping_cost = 20 + weight * 1.50

#Ground Shipping Premium
premium_shipping_cost = 125

#Drone Shipping
if weight > 10.0:
  drone_shipping_cost = weight * 14.25
elif weight > 6.0:
  drone_shipping_cost = weight * 12.00
elif weight > 2.0:
  drone_shipping_cost = weight * 9.00
else:
  drone_shipping_cost = weight * 4.50

#Compare price
if ground_shipping_cost < drone_shipping_cost:
  cost = ground_shipping_cost
  ground_transportation = True
else:
  cost = drone_shipping_cost
  drone_transportation = True

if premium_shipping_cost < cost:
  cost = premium_shipping_cost
  premium_transportation = True
  ground_transportation = False
  drone_transportation = False

#Final cost display
print("Method of transportation:")

if ground_transportation:
  print("Ground Shipping\n")
elif drone_transportation:
  print("Drone Shipping\n")
elif premium_transportation:
  print("Ground Shipping Premium\n")
else:
  print("Error\n")

print("Cost of shipping: $", cost)