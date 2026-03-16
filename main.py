# main.py
from processamento import validar_dados, calcular_media, gerar_relatorio_texto

# Dados de entrada conforme o briefing (Lista de Tuplas)
alunos_dados = [
    ("Alice", [8.5, 9.0, 7.8]),
    ("Bob", [6.0, 5.5, 6.5]),
    ("Charlie", []),            # Exemplo de lista vazia
    ("Daniel", [9.5, 10.0]),
    ("Eva", "dado_corrompido"), # Exemplo de dado inválido
    ("Frank", [7.0, 7.2, 6.8])
]

def iniciar_sistema():
    print("=" * 30)
    print("  PROCESSAMENTO SENAI  ")
    print("=" * 30)

    # 1. Validação de dados
    validos, falhas = validar_dados(alunos_dados)
    
    if falhas:
        print(f"Atenção! Dados ignorados para: {', '.join(falhas)}")

    resultados_finais = []
    melhor_aluno = ("", 0.0)

    # 2. Processamento (Loops e Filtros)
    print("\nCalculando médias...")
    for nome, notas in validos:
        media = calcular_media(notas)
        status = "Aprovado" if media >= 7.0 else "Recuperação"
        
        # Armazena para o relatório
        resultados_finais.append((nome, media, status))
        
        # Identifica o Top Student
        if media > melhor_aluno[1]:
            melhor_aluno = (nome, media)
        
        # Exibe no console
        print(f"Aluno: {nome:.<10} | Média: {media:.2f} | Status: {status}")

    # 3. Geração do Relatório Final (.txt)
    gerar_relatorio_texto(resultados_finais, melhor_aluno, falhas)
    print("\nProcessamento finalizado.")

if __name__ == "__main__":
    iniciar_sistema()