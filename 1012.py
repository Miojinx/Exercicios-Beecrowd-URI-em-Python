a, b, c = map(float, input().split())
areaTri = (a * c) / 2
print("TRIANGULO: %.3f" % areaTri)
areaCirc = 3.14159*c**2
print("CIRCULO: %.3f" % areaCirc)
areaTrap = ((a + b)*c) / 2
print("TRAPEZIO: %.3f" % areaTrap)
areaQuadr = b*b
print("QUADRADO: %.3f" % areaQuadr)
areaRet = a * b
print("RETANGULO: %.3f" % areaRet)