
from processamento import ler_arquivo_alunos, calcular_media, salvar_relatorio

def executar():
    print("--- SISTEMA SENAI: PROCESSANDO ARQUIVO EXTERNO ---")
    
    # Busca os dados no arquivo TXT
    dados = ler_arquivo_alunos("alunos.txt")
    
    processados = []
    erros = []
    melhor_aluno = ["", 0.0]

    for nome, notas in dados:
       
        if len(notas) > 0:
            media = calcular_media(notas)
            status = "Aprovado" if media >= 7.0 else "Recuperacao"
            processados.append((nome, media, status))
            
            
            if media > melhor_aluno[1]:
                melhor_aluno = [nome, media]
        else:
            erros.append(nome)

    salvar_relatorio(processados, melhor_aluno, erros)

if __name__ == "__main__":
    executar()