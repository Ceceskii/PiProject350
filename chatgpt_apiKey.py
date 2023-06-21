import openai

openai.api_key = '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'

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

