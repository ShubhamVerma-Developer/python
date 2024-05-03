from fastapi import FastAPI, HTTPException

app = FastAPI()

from openai import AzureOpenAI

@app.get("/")
async def fun():
    client = AzureOpenAI(
    azure_endpoint = "..........................", 
    api_key="........................",  
    api_version="2024-02-15-preview"
    )
    message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"what is java"}]
    completion = client.chat.completions.create(
    model="gpt-35-turbo", 
    messages = message_text,
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
    )
    return completion.choices[0].message.content


@app.post("/prompt/")
async def fun1(prompt: str):
    print(prompt)
    client = AzureOpenAI(
        azure_endpoint="<--api endpoint-->",
        api_key="<---key--->",
        api_version="2024-02-15-preview"
    )
    message_text = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": prompt}
    ]
    try:
        completion = client.chat.completions.create(
            model="gpt-35-turbo",
            messages=message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))