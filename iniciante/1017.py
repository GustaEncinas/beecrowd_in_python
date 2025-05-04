tempoGastoEmHoras = int(input())
velocidadeMediaEmKM = int(input())
litroDeGasolina = (tempoGastoEmHoras*velocidadeMediaEmKM)/12
print("{:.3f}".format(litroDeGasolina))