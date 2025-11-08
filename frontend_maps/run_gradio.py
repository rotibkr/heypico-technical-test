import gradio as gr
from maps_helper import search_places

def llm_query_with_maps(prompt):
    places = search_places(prompt)
    if "error" in places:
        return f"Error: {places['error']}"
    
    output = ""
    for p in places:
        output += f"[{p['name']}]({p['maps_url']}) - {p['address']}\n\n"
    return output

iface = gr.Interface(
    fn=llm_query_with_maps,
    inputs="text",
    outputs="markdown",
    title="Local LLM + Google Maps",
    description="Type prompt like 'cafe in Jakarta', Show result on Google Maps"
)

iface.launch()
