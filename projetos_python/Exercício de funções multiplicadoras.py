def smart_multiplier(multiplicador):
    def multiplier(numb):
      return multiplicador * numb
    return multiplier

duplicar = smart_multiplier(2)
triplicar = smart_multiplier(3)
quadriplicar = smart_multiplier(4)

print(duplicar(2))
print(triplicar(6))
print(quadriplicar(10))