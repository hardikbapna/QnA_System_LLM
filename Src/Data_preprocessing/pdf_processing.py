from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

import Src.Data_preprocessing.create_embeddings as embed


def read_pdf(file):

    loader= PyMuPDFLoader(file.name)   
    documents= loader.load()

    print("fn: read_pdf, completed")

    return documents


def text_process(document):
    text_splitter= CharacterTextSplitter(chunk_size= 1000, chunk_overlap= 20)
    texts= text_splitter.split_documents(document)

    print("fn: text_process, completed")

    return texts

def  call_embeds():
    embeddings= embed.embedding_creation()

    print("fn: call_embeds, completed")
    
    return embeddings

