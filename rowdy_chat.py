# import modules
import gradio as gr
import openai
import random
import time

# ENCRYPT LOL
openai.api_key = "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"

# create specialized chatGPT role: Rowdy Mascot
chat_log = [{"role": "system", "content": "You are an enthusiastic UTSA mascot named Rowdy. Keep answers to 25 tokens"}]

with gr.Blocks(css=".svelte-1ipelgc {color: #FFFFFF !important; background-color: #A84A17 !important} .svelte-1ipelgc:hover {background-color: #A73B00 !important} .download {opacity: 0} .svelte-1lyswbr {color: #003166 !important} #component-2 {background-color: #e88504; margin:auto; width: 40%; padding-bottom: 30p} #component-1 {background-color: #e88504; margin: auto; width: 40%; padding-top: 40px} body {background-color: #e88504} .gradio-container {background-color: #e88504; width: 60% !important}", theme=gr.themes.Soft(primary_hue="blue", secondary_hue="blue")) as chat:
    #image = gr.Image()
    
    img = gr.Image("https://www.utsa.edu/mbrs/resources/logos/Rowdy.png", show_label=False)
    img = gr.Image("https://i.imgur.com/SBVa06e.pngg", show_label=False)
    chatbot = gr.Chatbot(label="Rowdy")
    msg = gr.Textbox(label="You")
    clear = gr.Button("Clear chat")
    def user(user_message, history):
        chat_log.append({"role": "user", "content": user_message})
        return "", history + [[user_message, None]]

    def bot(history):
        
        response = openai.ChatCompletion.create(
        
        # Selects the chat model
            model="gpt-3.5-turbo",
            
            # Pass the message dictionary
            messages = chat_log
        )
        
        chat_log.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        
        #bot_message = random.choice(["Yes", "No"])
        history[-1][1] = response["choices"][0]["message"]["content"]
        time.sleep(1)
        #print(history[-1][0])
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

chat.launch()