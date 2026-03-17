# processamento.py

def ler_arquivo_alunos(nome_arquivo):
    lista_final = []
    try:
        # Usamos encoding utf-8 para aceitar acentos nos nomes
        arquivo = open(nome_arquivo, "r", encoding="utf-8")
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            
            # Divide o nome das notas pela virgula
            partes = linha.split(",")
            nome = partes[0]
            
            try:
                # Transforma as notas de texto para numeros
                notas = []
                for n in partes[1:]:
                    notas.append(float(n))
                lista_final.append((nome, notas))
            except:
                # Se a nota for invalida (ex: Eva), envia lista vazia
                lista_final.append((nome, []))
        arquivo.close()
    except FileNotFoundError:
        print("Erro: O arquivo alunos.txt nao foi encontrado!")
    return lista_final

def calcular_media(notas):
    # Funcao obrigatoria para o processamento
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def salvar_relatorio(resultados, destaque, erros):
    # Gera o arquivo final com o formato pedido
    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write("=== RELATORIO DE DESEMPENHO ACADEMICO - SENAI ===\n\n")
        
        for nome, media, status in resultados:
            f.write(f"Aluno: {nome:.<20} Media: {media:>5.2f} | Status: {status}\n")
        
        f.write("\n" + "="*45 + "\n")
        f.write(f"TOP STUDENT: {destaque[0]} com media {destaque[1]:.2f}\n")
        f.write("="*45 + "\n")
        
        if erros:
            f.write(f"\nDados ignorados para: {', '.join(erros)}\n")