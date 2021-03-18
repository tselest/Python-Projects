# **Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.

def tile():
    c = float(input("Cost per m^2: "))
    w = float(input("meters of the width: "))
    h = float(input("meters of the height: "))
    return c, w, h


def cost_tile():
    x,y,z = tile()
    print(f"The cost is: {(float(x * y * z)):.2f} $" )

if __name__ == "__main__":
    cost_tile()
