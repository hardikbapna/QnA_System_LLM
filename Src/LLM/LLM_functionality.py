from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI




#model_name= "text-davinci-003"
#model_name= "gpt-3.5-turbo"

def chain_creation(index_vector):

    #llm= OpenAI(openai_api_key=qna_test_api_key, model_name=model_name)
    
    
    chain = ConversationalRetrievalChain.from_llm(ChatOpenAI(temperature=0.3), 
                                   retriever=index_vector.as_retriever(search_kwargs={"k": 1}),
                                   return_source_documents=True)

    return chain    

