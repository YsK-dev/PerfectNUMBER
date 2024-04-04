

while True:
 muq=int(input("Mükemmel olup olmadığını merak ettiğin sayıyı Gir: "))

 bolumlerin_toplamı=sum(i for i in range(1,muq)if muq % i==0)


 if bolumlerin_toplamı == muq:
    print("mükemmelsin ve sayında mükemmel")
 else:
    print("NEin muq değil")