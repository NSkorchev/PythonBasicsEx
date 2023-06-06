# Read user input
degrees = int(input())
daytime = input()

# Logic
outfit = None
shoes = None

if 10 <= degrees <= 18:
    if daytime == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif daytime == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 <= degrees <=24:
    if daytime == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif daytime == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
else:
    if daytime == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif daytime == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
# Output
