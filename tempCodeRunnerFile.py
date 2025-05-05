def fun(x, y, z):
    if x > 0:
        z = z * 2
        fun(x - 2, y, z)
        y = y + 20
        fun(x - 1, y, z)
        print(x, y, z)
        fun(x - 2, y, z)
        
fun(4,5,6)