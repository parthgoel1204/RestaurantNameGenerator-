from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = groq_api_key

llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.6)

def generate_restaurant_name_and_items(cuisine):
  prompt_template_name = PromptTemplate(
      input_variables = ['cuisine'],
      template = "I want to open a restaurant for {cuisine} food . Suggest me one lucrative name!"
  )
  name_chain = LLMChain(llm = llm, prompt = prompt_template_name , output_key = "restaurant_name")

  prompt_template_items = PromptTemplate(
      input_variables = ['restaurant_name'],
      template = "Suggest some menu items for {restaurant_name}, Return it as a comma separated list"
  )
  food_items_chain = LLMChain(llm = llm, prompt= prompt_template_items, output_key = "menu_items") 

  chain = SequentialChain(
    chains = [name_chain,food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name','menu_items']
  )
  response = chain.invoke({'cuisine' : cuisine})
  return response

if __name__ == "__main__":
  cuisine = "Italian"
  response = generate_restaurant_name_and_items(cuisine)
  print(response)