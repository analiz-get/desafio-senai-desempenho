# Sistema de Acompanhamento Acadêmico - SENAI

## 1. Mapa de Empatia (Design Thinking)
- O que a Coordenação sente? Insegurança com dados manuais, sobrecarga de tempo e medo de erros.
- O que ela precisa? Agilidade, dados confiáveis e identificação rápida de alunos em recuperação ou destaque.

## 2. Levantamento de Requisitos

### Requisitos Funcionais (RF)
- RF01: Processar uma estrutura de dados (Lista de Tuplas).
- RF02: Validar se os dados estão completos ou corrompidos.
- RF03: Calcular a média aritmética de cada aluno (notas variáveis).
- RF04: Filtrar alunos em Recuperação (Média < 7.0).
- RF05: Identificar o "Top Student" (maior média).
- RF06: Gerar um relatório final em arquivo .txt.

### Requisitos Não-Funcionais (RNF)
- RNF01: Modularização (separação em main.py e processamento.py).
- RNF02: Versionamento organizado via Branches no Git.
- RNF03: Código limpo e organizado (padrão SENAI).

### Regras de Negócio (RN)
- RN01: A média mínima para aprovação é 7.0.
- RN02: Alunos sem notas ou com dados corrompidos devem ser tratados/avisados.

## 3. Kanban (Gestão Ágil)
- [x] Levantamento de Requisitos e README (Done)
- [x] Criar estrutura modular de arquivos (.py) (Done)
- [x] Implementar validação e tratamento de dados (Done)
- [x] Implementar lógica de médias e filtros (Done)
- [x] Gerar relatório .txt e finalizar documentação (Done)