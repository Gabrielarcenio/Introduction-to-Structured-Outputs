# Extractor de Informações

Este projeto utiliza a API da OpenAI para extrair automaticamente tarefas, prazos e responsáveis de textos, como e-mails ou documentos de projeto.

## Funcionalidades

- **Extração de Tarefas**: Identifica tarefas mencionadas em um texto.
- **Identificação de Prazos**: Extrai datas que servem como prazos para as tarefas.
- **Determinação de Responsáveis**: Aponta as pessoas responsáveis por cada tarefa identificada.

## Tecnologias Utilizadas

- Python
- OpenAI API

## Configuração

Para rodar este projeto, você precisa configurar uma chave de API da OpenAI. Defina a chave API em seu ambiente como `OPENAI_API_KEY`.

```bash
export OPENAI_API_KEY='sua_chave_aqui'
