
def call_chat_model(client, messages):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=1,
        max_tokens=4096
    )