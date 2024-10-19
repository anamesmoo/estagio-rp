def count_letter_a(string):
    # Convertendo a string para minúsculas para contar 'a' e 'A' de forma case-insensitive
    string_lower = string.lower()
    
    # Contando o número de ocorrências da letra 'a'
    count = string_lower.count('a')
    
    # Retornando a quantidade e se a letra 'a' existe ou não
    if count > 0:
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

# Solicitando uma string do usuário
text = input("Digite uma string: ")

# Verificando a existência e a quantidade de 'a'
count_letter_a(text)
