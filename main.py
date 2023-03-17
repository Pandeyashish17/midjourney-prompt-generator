import gradio as gr
import openai
from gradio.components import Textbox,Button
import pyperclip

def generate_prompt(keywords,api_key):
    openai.api_key = api_key
    messages = [
        {"role": "system", "content": '''
         this is an example prompt i got from the keyword "Astronout walking on mars": "Astronaut walking on the red dusty surface of Mars, collecting samples of its soil, rocks, and atmosphere. With every step, they are discovering new and exciting things about this alien world." here is another example of "A dragon taking over the world": "Dragon, flying across the world. Its wings were so large that they cast a shadow over the land, blocking out the sun. Its fire was so powerful that it could turn entire cities to ash in a matter of moments." now i will give you some keywords and generate the prompt based on those keywords like those above example. now i will give you some keywords. and also keep the prompt like keywords based that will enhance the image 
         '''},
        {"role": "user", "content": keywords},
       
    ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content



api_key_input = Textbox(label="Then go to this https://platform.openai.com/account/api-keys generate secret key and paste it here",placeholder = "eg: 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")

keywords_input = Textbox(label="Keywords you want in your description", placeholder="eg: A dragon taking over the world")


output_text = Textbox(label="Prompt",placeholder= '''Dragon, flying across the world. Its wings were so large that they cast a shadow over the land, blocking out the sun. Its fire was so powerful that it could turn entire cities to ash in a matter of moments.
''')


description = "Use OpenAI's GPT-3.5 turbo model (ChatGPT) to generate a midjourney prompt based on user keywords."

examples = [
    ["A backpack made entirely of human hair."],
    ["A bicycle with wheels made out of jelly."],
    ["A jacket made entirely out of old computer keyboards."],
    ["A bookshelf made entirely out of ice that slowly melts over time."],
    ["a chair made out of pizza slices"],
    ["a banana with a bow tie and a top hat"],
    ["a surreal landscape with floating islands"],
    ["a cat made out of clouds"],
    ["a piano that also functions as a fish tank"],
    ["a treehouse made entirely of recycled materials"],
    ["a motorcycle with 8 wheels"],
    ["a sculpture of a giant snail made entirely of cheese"],
    ["a house with a living tree growing through the middle"],
    ["a car covered entirely in mirrors"],
    ["a suit made out of recycled plastic bottles"],
    ["a bicycle with square wheels"],
    ["a set of cutlery made entirely of candy"],
    ["a chandelier made of human hair"],
    ["a giant rubber duck that can be used as a bathtub"],
    ["a coat made of feathers from every bird species in the world"],
    ["a lamp that is also a plant"],
    ["a chair that is also a rocking horse"],
    ["a pair of glasses that allow you to see through walls"],
    ["a house with a slide instead of stairs"],
    ["a motorcycle with a built-in hot tub"],
    ["a dress made entirely of recycled paper"],
]

gr.Interface(
    fn=generate_prompt, 
    inputs=[keywords_input,api_key_input], 
    outputs=output_text,
    description=description,
    examples= examples
).launch()
