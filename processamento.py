
def ler_arquivo_alunos(nome_arquivo):
    lista_final = []
    try:
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
        for linha in arquivo:
            partes = linha.strip().split(";")
            if len(partes) < 2:
                continue
            
            nome = partes[0]
            try:
                notas_texto = partes[1].split(",")
                notas_float = []
                for n in notas_texto:
                    if n != "":
                        notas_float.append(float(n))
                lista_final.append((nome, notas_float))
            except:
                lista_final.append((nome, [])) # dado corrompido
        arquivo.close()
    except FileNotFoundError:
        print("Erro: O arquivo alunos.txt nao foi encontrado!")
    return lista_final

def calcular_media(notas):
    return sum(notas) / len(notas)

def salvar_relatorio(resultados, destaque, erros):
    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write("=== RELATORIO DE DESEMPENHO ACADEMICO ===\n\n")
        for nome, media, status in resultados:
            f.write(f"Aluno: {nome:.<20} Media: {media:>5.2f} | Status: {status}\n")
        
        f.write("\n" + "="*40 + "\n")
        f.write(f"TOP STUDENT: {destaque[0]} com media {destaque[1]:.2f}\n")
        f.write("="*40 + "\n")
        
        if erros:
            f.write(f"\nDados invalidos/ausentes para: {', '.join(erros)}\n")
    print("Relatorio gerado com sucesso no arquivo 'resultado.txt'!")