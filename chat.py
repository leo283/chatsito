import openai
from os import getenv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(".env")

client = OpenAI()
openai.api_key=getenv('OPENAI_API_KEY')

def create_response(content):
  response = client.chat.completions.create(
    model = "gpt-4-1106-preview",
    messages=[{
      "role":"user",
      "content":content
    }]
  )
  return response.choices[0].message.content

def main():
  print("Type 'quit' to exit")
  while True:
    content = input("Escribe algo: ")
    if content == "quit":
      break
    print(create_response(content))