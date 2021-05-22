import matplotlib.pyplot as plt
fig=plt.figure(u"lenguajes de programacion")
ax= fig.add_subplot(111)
nombres=["PYTHON" ,"java" ,"javascrip","c#", "php" ,"r","objetive-c" ,"swift","matlab","typescrip","rudy"]
datos=[26,21,8,7,6,6.8,4,3,2.56,2.04,1.57,1.53]
xx=range(len(datos))
ax.bar(xx,datos,width=0.8,aling="center",color="blue")
ax.set_xticks(xx)
ax.set_xtickslabels(nombres)
plt.title("lenjuages de programacion")
plt.legend("1")
plt.xlabel("lenguajes")
plt.ylabel("cantidad")
plt.savefig("pytin.png")
plt.savefig("python.jpg")
plt.savefig("pyyhon.pdf")
plt.show()