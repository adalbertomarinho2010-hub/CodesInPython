import copy as cp

ano_2026 = [["Garchomp","Gengar","Greninja"],[15, 11, 20] ,[2000,1500,1000]]
print (ano_2026)
ano_2027 = cp.deepcopy(ano_2026)
ano_2027[0][0] = "Greninja"
ano_2027[1][0] = 22
print (ano_2027)
ano_2028 = cp.deepcopy(ano_2026)
ano_2028[0][0] = "Gardevoir"
ano_2028[1][0] = 33
print (ano_2028)