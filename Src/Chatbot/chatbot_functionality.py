import gradio as gr
#from app import chain



chat_history=[]

def return_chain_fn(chain_alias):
    global chain
    chain=chain_alias


def add_text(history, message):
    if not message:
        raise gr.Error("Enter some text!")
    else:
        history+=[(message," ")]

    return history


def generate_response(history, query, btn):
    
    global chat_history
    '''
    if not btn:
        raise gr.Error("First upload a PDF file!!")
    if Count == 0:
    '''

    result= chain({"question": query, 'chat_history':chat_history}, return_only_outputs=True)

    chat_history += [(query, result["answer"])]

    for char in result['answer']:
        history[-1][-1] += char

        yield history, ''
        
