import os
import openai

# Configuração da chave API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Função para analisar o documento e extrair informações usando o endpoint de chat
def extract_info_from_text(text):
    try:
        # Chamada à API usando o endpoint de chat
        response = openai.ChatCompletion.create(
          model="gpt-4",  # Usando o modelo GPT-4 adequado para chat
          messages=[
              {"role": "system", "content": "You are a smart assistant."},
              {"role": "user", "content": f"Extract tasks, deadlines, and responsible parties from the following text:\n\n{text}"}
          ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Exemplo de texto para processamento
email_text = """
Dear team,

Please remember to update the project documentation by next Friday, March 26th. John will be responsible for the final review and submission.

Also, ensure that the client presentation is ready for the demo on March 30th. Sarah and Mike will handle the preparations.

Best,
Management
"""

# Chamada da função
extracted_info = extract_info_from_text(email_text)
print("Extracted Information:\n", extracted_info)
