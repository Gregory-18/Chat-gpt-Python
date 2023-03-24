#Importamos las librerias
import openai
import config #modulo donde esta la api_key

#configuramos la api_key
openai.api_key = config.api_key

#definimos el contexto del asistente
messages = [{'role':'system', 
             'content': 'Eres un asistente'}]

#definimos el mensaje
content = input('Sobre que quieres hablar?')

#definimos el rol de usuario
messages.append({'role':'user', 'content': content})

#definimos la respuesta
response = openai.ChatCompletion.create(model='gpt-3.5-turbo',
                                        messages=messages)

#Se imprime la respuesta
print(response.choices[0].message.content)