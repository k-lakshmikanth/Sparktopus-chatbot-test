from gpt4all import GPT4All
import os

try:
    os.mkdir("models")
except FileExistsError:
    pass

model = GPT4All("wizardLM-13B-Uncensored.ggmlv3.q4_0.bin", model_path=os.path.join(os.getcwd(),"models"))

with model.chat_session():
    os.system("cls")
    prompt = input(">> ")
    while prompt != "exit":
        chat = model.generate(prompt)
        print(chat)
        prompt = input(">> ")
