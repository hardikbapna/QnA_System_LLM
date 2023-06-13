import pinecone
from langchain.vectorstores import Pinecone
import os
from dotenv import load_dotenv
load_dotenv()



pinecone_environment= "us-west1-gcp-free"
index_name= "qna-system-openai-1536-dim"


def initialize_pinecone():
    pinecone.init(
    #api_key= pinecone_api_key,
    environment= pinecone_environment
    )
    print("Initialized the Pinecone instance.")
    
    index= pinecone.Index(index_name)
    #name_space= detect_namespace(index)
    delete_vector(index)
    

    """
    delete_response= index.delete(deleteAll= True)
    print("Deleted the vectors in pinecone index.")
    """

'''   
def detect_namespace(index):
    index_stats= index.describe_index_stats()
    name_space= list(index_stats['namespaces'].keys())
    print(name_space)
    
    return name_space
    '''



def delete_vector(index):
    #index= pinecone.Index(index_name) 
    delete_response= index.delete(deleteAll= True)
    print("Deleted the vectors in pinecone index.")

    #return index


def save_vector(texts, embeddings):
    index_vector= Pinecone.from_documents(texts, embeddings, index_name= index_name)

    return index_vector   


#initialize_pinecone()
