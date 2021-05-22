
import matplotlib.pyplot as plt
eje_x =[ "minicraf","wii sports","gta v","tetris","arg" ]
eje_y =[ "360000000000", "829000000", "145000002", "100000", "7000000" ]
color =["red","blue","black","purple","orange" ]
plt.bar(eje_x, eje_y, color-color)
plt.ylabel("ventas (100 millones)")
plt.xlabel( "videsjuegos" )
plt.title( "videojuegos mas vendidos" )
plt.savefig( "videojuegos mas vendidos.png" )
plt.show()
 