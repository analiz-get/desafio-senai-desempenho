# processamento.py

def validar_dados(alunos):
    """
    Verifica se a estrutura de notas é uma lista válida e não vazia.
    """
    dados_validos = []
    erros = []
    for nome, notas in alunos:
        # Valida se notas é uma lista, se não é string (corrompido) e se tem conteúdo
        if isinstance(notas, list) and len(notas) > 0:
            dados_validos.append((nome, notas))
        else:
            erros.append(nome)
    return dados_validos, erros

def calcular_media(notas):
    """Calcula a média simples de uma lista de números."""
    return sum(notas) / len(notas)

def gerar_relatorio_texto(resultados, top_student, falhas):
    """Gera o arquivo resultado.txt formatado."""
    try:
        with open("resultado.txt", "w", encoding="utf-8") as f:
            f.write("=== RELATÓRIO ACADÊMICO SENAI ===\n")
            f.write("-" * 33 + "\n\n")
            
            f.write("DESEMPENHO POR ALUNO:\n")
            for nome, media, status in resultados:
                f.write(f"Nome: {nome:.<15} Média: {media:>5.2f} | Status: {status}\n")
            
            f.write("\n" + "="*33 + "\n")
            f.write(f"DESTAQUE: {top_student[0]} (Média: {top_student[1]:.2f})\n")
            f.write("="*33 + "\n")
            
            if falhas:
                f.write(f"\nAVISO: Dados inválidos/ausentes para: {', '.join(falhas)}\n")
        
        print("\n[SUCESSO] Arquivo 'resultado.txt' gerado com êxito!")
    except Exception as e:
        print(f"Erro ao gerar relatório: {e}")