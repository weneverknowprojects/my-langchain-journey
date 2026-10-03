from color import Color
from llm import generate_launching_product, generate_launching_product_with_pydantic_parser_output


def main():
    print("Hello from structured-data-generator!")


if __name__ == "__main__":
    print("Launching Product Generator for Sales & Marketing")
    productName = input("what is your new product? \n")
    if productName == "":
        print("product name is required. will exit app")
        exit(1)

    detailProduct = input("tell me about your new product! \n")

    print(f"{Color.DIM}Please wait while we generate a structured output for your product: {productName} with details: {detailProduct}")
    print(f"{Color.DIM}.........................................\n")
    generate_launching_product_with_pydantic_parser_output(productName, detailProduct)
    # generate_launching_product(productName, detailProduct)
        

