import gradio as gr
import openai
from gradio.components import Textbox

def generate_prompt(api_key, keywords):
    openai.api_key = api_key
    messages = [
        {"role": "system", "content": '''
         this is an example prompt i got from the keyword "ocean": "Create the image of a beautiful ocean, with waves crashing against the shore. The water is a deep blue, with hints of green in the shallower areas. In the foreground, there is a sandy beach with seashells and driftwood scattered along the shoreline. In the distance, there is a rocky island with steep cliffs rising up from the water." here is another example of mountain: "Create the image of a majestic mountain range, with snow-capped peaks rising up into the clouds. In the foreground, there is a dense forest with towering trees, their leaves creating a canopy overhead that filters the sunlight into dappled patterns on the ground below. The sky is a deep blue, with hints of pink and orange in the clouds that are catching the light of the setting sun." now i will give you some keywords and generate the descritption based on those keywords. add the details u want which will be cool to have and generate only description.  Your description should be vivid and explanatory, providing clear details of the image's composition, color scheme, and overall aesthetic. Additionally, feel free to add any additional details or features that you believe would enhance the image. now i will give you some keywords
         '''},
        {"role": "user", "content": keywords},
       
    ]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content

api_key_input = Textbox(label="go to this https://platform.openai.com/account/api-keys and generate secret key")
keywords_input = Textbox(label="Keywords you want in your description")
output_text = Textbox(label="Prompt")

description = "Use OpenAI's GPT-3.5 turbo model (ChatGPT) to generate a midjourney prompt based on user keywords."

gr.Interface(
    fn=generate_prompt, 
    inputs=[api_key_input, keywords_input], 
    outputs=output_text, 
    description=description
).launch()
