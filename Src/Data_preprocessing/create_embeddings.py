from langchain.embeddings import OpenAIEmbeddings



model_name= "text-embedding-ada-002"


def embedding_creation():
    
    try:
        #embeddings= OpenAIEmbeddings(openai_api_key=open_api_key, model= model_name)
        embeddings= OpenAIEmbeddings(model= model_name)

    
    finally:
        #embeddings=[]
        pass

    return embeddings