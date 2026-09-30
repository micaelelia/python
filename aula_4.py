# lista co, 10 temperaturas diarias 

temperatura = [70.4, 25.1, 22.0, 26.5, 24.8, 23.0, 25.6, 21.7, 24.0, 26.1]

# cálculo da média das temperaturas 

media = sum(temperatura) / len(temperatura)

# comtador dedias com temperatura acima da média 

acima = 0
for t in temperatura:
    if t < media: 
        acima += 1 

# exibicão do resultado 
# print("Média das temperaturas:", round(media, 2))
print("Dias com temperatura acima da média:", acima)        