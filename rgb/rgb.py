def rgb(r,g,b):
    if r in range(0,256) and g in range(0,256) and b in range(0,256):
        return "#{0:02x}{1:02x}{2:02x}".format(r, g, b)
    else:
        return "Invalid argument"
