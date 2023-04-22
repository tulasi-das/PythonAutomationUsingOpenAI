# OpenAPI Key: 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
import requests


api_endpoint = "https://api.openai.com/v1/completions" #api endpoint for text completions
api_key =  "" #your open ai api key

print("enter your question")
enter_your_question = input() # prompt that you want to ask chat gpt


request_header = {   # request header containig api key for authorization
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_body ={
  "model": "text-davinci-003", # open ai model
  "prompt": enter_your_question,  #you question
  "max_tokens": 100,
  "temperature": 0.5
}

response = requests.post(api_endpoint,headers = request_header, json = request_body) #requesting open ai api throught post method

if response.status_code == 200:
    print(response.json()["choices"][0]["text"])  # printing the response
else:
    print(f"response failed: {str(response.status_code)}") # if there is an error print the response code
