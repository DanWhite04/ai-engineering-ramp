import os 
from dotenv import load_dotenv
import anthropic

load_dotenv(override=True)         
client = anthropic.Anthropic()     

def main():
    messages = []
    messages.append({"role": "user", "content": "Suggest a weekend trip in Australia for someone who loves hiking."})
    print("Claude: ", end="", flush=True)

    with client.messages.stream(
        model="claude-haiku-4-5",
        max_tokens=300,
        messages=messages
    ) as stream:
        assistant_reply = ""
        for text in stream.text_stream:
            print(text, end="", flush=True)
            assistant_reply += text
            print()
    messages.append({"role": "assistant", "content": assistant_reply})    

    messages.append({"role": "user", "content": "What about for someone who prefers beaches instead?"})
    print("Claude: ", end="", flush=True)

    with client.messages.stream(
        model="claude-haiku-4-5",
        max_tokens=300,
        messages=messages
    ) as stream:
        assistant_reply = ""
        for text in stream.text_stream:
            print(text, end="", flush=True)
            assistant_reply += text
            print()
    messages.append({"role": "assistant", "content": assistant_reply}) 

if __name__ == "__main__":
    main()