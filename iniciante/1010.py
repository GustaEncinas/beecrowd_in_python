a, b, c = map(float, input().split())
a2, b2, c2 = map(float, input().split())
val = (b * c)+(b2 * c2)
print("VALOR A PAGAR: R$ {:.2f}".format(val))