# main.py
from processamento import ler_arquivo_alunos, calcular_media, salvar_relatorio

def executar_sistema():
    print("--- SISTEMA SENAI: PROCESSANDO 40 ALUNOS ---")
    
    # 1. Carrega os dados do arquivo externo
    dados = ler_arquivo_alunos("alunos.txt")
    
    alunos_processados = []
    alunos_com_erro = []
    melhor_aluno = ["Ninguém", 0.0]

    # 2. Processa cada aluno da lista
    for nome, notas in dados:
        # Valida se a lista de notas nao esta vazia (Requisito RNF)
        if len(notas) > 0:
            media = calcular_media(notas)
            
            # Define o status
            status = "Aprovado" if media >= 7.0 else "Recuperacao"
            
            alunos_processados.append((nome, media, status))
            
            # Verifica se e o Top Student
            if media > melhor_aluno[1]:
                melhor_aluno = [nome, media]
        else:
            alunos_com_erro.append(nome)

    # 3. Gera o arquivo de bônus resultado.txt
    salvar_relatorio(alunos_processados, melhor_aluno, alunos_com_erro)
    
    print(f"Processamento concluido! {len(alunos_processados)} alunos listados.")
    print("Abra o arquivo 'resultado.txt' para ver o detalhamento.")

if __name__ == "__main__":
    executar_sistema()

    