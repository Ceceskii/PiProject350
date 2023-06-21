# original draft from https://pimylifeup.com/raspberry-pi-chatgpt/

import openai

openai.api_key = 'SECRETKEY'

messages = [ {"role": "system", "content": "You are an intelligent assistant." } ]

while True:
    message = input("You: ")

    messages.append(
        {"role": "user", "content": message},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message

    print("Assistant: ", reply.content)
    
    messages.append(reply)
