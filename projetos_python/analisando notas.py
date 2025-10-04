def notas(* n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
      if r['Média'] >= 7:
        r['Situação'] = 'BOA'
      elif r['Média'] >= 5:
        r['Situação'] = 'Razoavel'
      else:
         r['Situação'] = 'ruim'
    return r         
resp = notas(5.5 , 2.5, 9, 8.5)
print(resp)