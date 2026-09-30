#funções sempre tem que ter indentação
#def big_mac():
 #   print("sanduiche big mac")

#print("incio")
#big_mac()
#print("fim")

def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")  


def fazer_batata(tamanho):
    print(f"batata {tamanho}") 


def preparar_refrigerante(tipo,tamanho):
    print(f"{tipo} {tamanho}") 

#fazer_big_mac("roger")
#fazer_batata("grande")   
#preparar_refrigerante("coca","media") 


def fazer_combo_big_mac(nome,tamanho_batata,tipo_refri,tamnho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri,tamnho_refri)

#fazer_combo_big_mac("roger","grande","coca","media")    

