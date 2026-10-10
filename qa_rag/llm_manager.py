from langchain_openrouter import ChatOpenRouter

model = ChatOpenRouter(
    model="dots-studio/dots-3-note-preview:free",
    temperature=0.2,
    max_tokens=1024,
    max_retries=2,    
)

def send_message(query:str, context:str):
    try:
        messages = [
               (
                   "system",
                   "You are a helpful assistant. You will be given a query and context. You need to provide a relevant answer based on the context."
               ),
               (
                   "user",
                   f"Query: {query}\nContext: {context}"
               )
            ]
        response = model.invoke(messages)
        return response
    except Exception as e:
        print(f"error send_messagev{e}")
