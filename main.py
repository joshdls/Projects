from art import logo
import math

def inches(user_width, user_length):
  unit_sqft = round((width/12) * (length/12),2)
  print(f"Product covers: {unit_sqft} sqft")
  return unit_sqft
  
  
def feet(user_width, user_length):
  unit_sqft = round((width * length), 2)
  print(f"Product covers: {unit_sqft} sqft")
  return unit_sqft
  

def piece(unit_size,size_of_space):
  pieces_needed = math.ceil(size_of_space / unit_size)
  print(f"Pieces_needed(rounded): {pieces_needed}")
  return pieces_needed
  
print(logo)
print("Square Footage Calculator")

unit_of_product = input("Is product sold by piece[p] or carton[c]?: ").lower()

if unit_of_product == 'p':

  unit_of_measurement = input("Measurement of product in inches[i] or feet[f]?:").lower()
  
  width = float(input("Width of product: "))
  length = float(input("Length of product: "))
  
  if unit_of_measurement == 'i':
    unit_sqft = inches(user_width = width, user_length = length)
  elif unit_of_measurement == 'f':
    unit_sqft = feet(user_width = width, user_length = length)
  
  space_size = float(input("Area of coverage size(sqft): "))
  
  pieces_needed = piece(unit_size = unit_sqft, size_of_space = space_size)
  price_of_unit = float(input("How much is each piece?: $"))
  price_of_size = price_of_unit * pieces_needed
  print(f"Price of pieces needed: ${price_of_size}")
  box_check = input("Is there a box count[y/n]?: ")
  if box_check == 'y':
    box_count = int(input("How many in box?: "))
    box_total = math.ceil(pieces_needed/box_count)
    print(f"Boxes needed(rounded): {box_total}")
    print(f"price of {box_total} boxes: ${(price_of_unit * box_count) * box_total} ")
    print(f"Extra pieces: {(box_total * box_count)-pieces_needed}")
  elif box_check == 'n':
    pass

if unit_of_product == 'c':
  square_of_carton = float(input("Carton Square footage?: "))
  cost_of_carton = float(input("Cost of carton?: $"))
  space_size = float(input("Area of coverage size(sqft): "))
  carton_cover_space = math.ceil(space_size / square_of_carton)
  print(f"Cartons needed(rounded): {carton_cover_space}")
  print(f"Cost of {carton_cover_space} cartons: ${cost_of_carton * carton_cover_space} ")
  print(f"Extra Sqft: {abs(space_size -(carton_cover_space * square_of_carton))}")
  
  
  


  


