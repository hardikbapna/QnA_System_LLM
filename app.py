import gradio as gr
import copy
import os
from dotenv import load_dotenv
load_dotenv()


import Src.Data_preprocessing.pdf_processing as pr
from Src.Pinecone_setup import pinecone_vectordb_setup as vect_db
import Src.Chatbot.chatbot_functionality as chat_func
import Src.LLM.LLM_functionality as llm_func






with gr.Blocks() as demo:

    with gr.Column():
        with gr.Row():
            with gr.Column(scale=0.8):
                api_key= gr.Textbox(
                    placeholder="Enter OpenAI API key",
                    show_label=False,
                    interactive=True
                ).style(container=False)
            with gr.Column(scale=0.2):
                change_api_key= gr.Button(
                    value= "Change Key!",
                    interactive= True
                )

        with gr.Row():
            with gr.Column(scale=0.8):
                pinecone_api_key= gr.Textbox(
                    placeholder="Enter Pinecone API key",
                    show_label=False,
                    interactive=True
                ).style(container=False)
            with gr.Column(scale=0.2):
                set_pinecone_api_key= gr.Button(
                    value= "Set Key!",
                    interactive= True
                )


        with gr.Row():
            chatbot= gr.Chatbot(
                value=[],
                elem_id="chatbot"
            ).style(height=680)

        with gr.Row():
            with gr.Column(scale=0.7):
                txt= gr.Textbox(
                    placeholder= "Ask your query here and press enter!",
                    show_label=False,
                    interactive=True
                ).style(container=False)
            with gr.Column(scale=0.15):
                submit= gr.Button("Submit")
            with gr.Column(scale=0.15):
                btn= gr.UploadButton("Upload PDF", file_types=['.pdf']).style()

        with gr.Row():    
            with gr.Column(scale=0.10):
                proc_btn= gr.Button(value= "Process uploaded data").style()

    



    
    
    def pdf_upload(file):
        #pr.read_pdf(file)
        print("Read successfully!")
        
        return "Uploaded successfully"


    def process_data(file):

        #Read file
        document= pr.read_pdf(file)
        texts= pr.text_process(document)
        embeddings= pr.call_embeds()
        
        #Deleting all vectors in Pinecone index and inserting the new vectors in that namespace. 
        vect_db.initialize_pinecone()
        index_vector= vect_db.save_vector(texts, embeddings)
        #index_vector=["This is demo", 78]

        #Calling function to create a ChatOpenAI chain.
        
        chain_alias= llm_func.chain_creation(index_vector)

        chat_func.return_chain_fn(chain_alias)
        

        print("fn: process_data, completed")

        
        return "Data Processed"
        


    def set_api_key(api_key):
        os.environ['OPENAI_API_KEY'] = api_key
        print("API key has been set to: ", os.environ['OPENAI_API_KEY'] )

        return "Open AI Api key set!!"
    

    def seting_pinecone_api(pinecone_api_key):
        os.environ['PINECONE_API_KEY'] = pinecone_api_key
        print("Pinecone API key has been set to: ", os.environ['PINECONE_API_KEY'] )

        return "Pinecone Api key set!!"
    

    
    
    
    
    
    #Set up Event Handlers

    #Event Handler for submitting OpenAI api key.
    #api_key.submit(fn=set_apikey, inputs=[api_key], outputs=[api_key])

    #Event Handler for setting OpenAI api key.
    change_api_key.click(fn=set_api_key, inputs= [api_key])

    #Event Handler for setting Pinecone api key.
    set_pinecone_api_key.click(fn=seting_pinecone_api, inputs= [pinecone_api_key])

    #Event handler for uploading PDF.
    btn.upload(fn= pdf_upload, inputs= [btn])
    
    #index_vector_exp= 
    proc_btn.click(fn= process_data , inputs=[btn], outputs=[gr.component("text")])

    #Event Handler for submitting text and generating response.
    submit.click(
        fn= chat_func.add_text,
        inputs= [chatbot, txt],
        outputs= [chatbot],
        queue= False
    ).success(
            fn= chat_func.generate_response,
            inputs= [chatbot, txt, btn],
            outputs= [chatbot, txt]
        )
    







demo.queue()
demo.launch(share=True)
