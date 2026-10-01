from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Say hello to my electronic component fault diagnosis project."
)

print(response.output_text)