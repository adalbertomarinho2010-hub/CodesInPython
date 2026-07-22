# def valorPagamento (valor_prestacao, dias_atraso):
#     valor_final = valor_prestacao + (valor_prestacao * 0,03) + (valor_prestacao * 0,001 * dias_atraso)
#     if dias_atraso == 0:
#         return valor_prestacao
#     return valor_final
# valor_final = 0
# quantidade = 0

# While True:
#     try:
#         valor_prestacao = float (input("\nDigite o valor da prestação: "))
#     except ValueError:
#         print ("\n *** Por favor, digite um número válido ***")
#     if valor_prestacao == 0:
#         break