from langchain_openrouter import ChatOpenRouter

from launching_product_model import LaunchingProductModel

from langchain_core.prompts import PromptTemplate

model = ChatOpenRouter(
    model="google/gemma-4-26b-a4b-it:free",
    temperature=0.7,
    max_tokens=1024,
    max_retries=2,    
)

def generate_response(prompt):
    response = model.generate(prompt)
    return response

def generate_launching_product(product:str, description: str):
    # combine prompt with user input as template prompt
    prompt = PromptTemplate.from_template("A new variant for next week's open pre-order batch: {product} with following details {description}")
    # convert promptTemplate to string
    userPrompt = prompt.format(product=product, description=description)
    messages = [
       (
           "system",
           "You are a product marketing assistant. You will be given a product description and you need to generate a structured output in the form of a LaunchingProductModel. The product description will include the product name, tagline, marketing copy, open purchase order details, SEO keywords, and social media"
       ),
       (
           "user",
              userPrompt
       )
       
    ]  
    # "A new variant for next week's open pre-order batch: a fried bun filled with smoked beef and melted mozzarella."  
    # parse LLM response to follow LaunchingProductModel
    model_structured_data = model.with_structured_output(LaunchingProductModel)
    # call LLM API with message
    response = model_structured_data.invoke(messages)
    
    print(str(response))

if __name__ == "__main__":
    generate_launching_product("Cheese Burger", "A delicious cheese burger with fresh ingredients.")