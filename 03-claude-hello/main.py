import os 
from dotenv import load_dotenv
import anthropic
from pydantic import BaseModel

load_dotenv(override=True)
client = anthropic.Anthropic()

class CapitalInfo(BaseModel):
    country: str
    capital : str
    population : str
    founded_year : str
    fun_fact : str

def main():
    tool_block = next(b for b in response.content if b.type == "tool_use")
    info = CapitalInfo(**tool_block.input)
    print(f"Country: {info.country}")
    print(f"Capital: {info.capital}")
    print(f"Population: {info.population}")
    print(f"Founded: {info.founded_year}")
    print(f"Fun fact: {info.fun_fact}")
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=500,
    tools=[
        {
        "name": "capital_info",
        "description": "Provide structured information about a country's capital city.",
        "input_schema": CapitalInfo.model_json_schema(),
        }
    ],
    tool_choice={"type": "tool", "name": "capital_info"},
    messages=[
        {"role": "user", "content": "Tell me about the capital of Australia."}
    ],
    system="You are an ethusiastic travel guide, make the facts memorable and interesting to the ones asking."
)

if __name__ == "__main__":
    main()
