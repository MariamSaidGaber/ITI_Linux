#Chat gpt with python
#Unforteuntly it is not available in our country

import os
import openai
openai.api_key = os.getenv.("Your API key")

completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
											messages=[
												     {"role":"user","content":"Welcome!"}
												     ]					
										)
										
print(completion.choices[0].message.content)



###########  Text Generation ############
# One of the most popular use cases for the OpenAI API is text generation. You can provide a prompt to the API, and it will generate text that continues from that prompt.

import openai
openai.api_key = "YOUR_API_KEY"

prompt = "The quick brown fox"
response = openai.Completion.create(
  engine="davinci-003",
  prompt=prompt,
  max_tokens=50
)

generated_text = response.choices[0].text.strip()
print(generated_text)


########### Language Translation ######################################
# The OpenAI API also supports language translation. You can provide a piece of text in one language and ask the API to translate it into another language.
import openai
openai.api_key = "YOUR_API_KEY"

text = "Hello, how are you?"
response = openai.Completion.create(
  engine="davinci",
  prompt=f"Translate from English to Spanish: {text}",
  max_tokens=50
)

translation = response.choices[0].text.strip()
print(translation)




########## Sentiment Analysis ####################################
# You can also use the OpenAI API for sentiment analysis. Given a piece of text, the API will tell you whether it has a positive or negative sentiment

import openai
openai.api_key = "YOUR_API_KEY"

text = "I love ice cream!"
response = openai.Completion.create(
  engine="davinci",
  prompt=f"Sentiment analysis: {text}",
  max_tokens=1
)

sentiment = response.choices[0].text.strip()
print(sentiment)








######### Question-Answering ########
#The OpenAI API also supports question-answering. You can provide a context and a question, and the API will return an answer based on that context

import openai
openai.api_key = "YOUR_API_KEY"

context = "Albert Einstein was a German-born theoretical physicist who developed the theory of relativity."
question = "Where was Albert Einstein born?"
response = openai.Completion.create(
  engine="davinci-003",
  prompt=f"Question answering:\nContext: {context}\nQuestion: {question}",
  max_tokens=50
)

answer = response.choices[0].text.strip()
print(answer)


############## Summarization ###########
#You can also use the OpenAI API for summarization. Given a long piece of text, the API will generate a summary that captures the most important information
import openai
openai.api_key = "YOUR_API_KEY"

text = "Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. We show that the use of such a large and diverse dataset leads to improved robustness to accents, background noise and technical language. Moreover, it enables transcription in multiple languages, as well as translation from those languages into English. We are open-sourcing models and inference code to serve as a foundation for building useful applications and for further research on robust speech processing."
response = openai.Completion.create(
  engine="davinci",
  prompt=f"Summarize:\n{text}",
  max_tokens=50
)

summary = response.choices[0].text.strip()
print(summary)



############ Code Generation ###########
#Finally, you can use the OpenAI API for code generation. You can provide a natural language description of what you want your code to do, and the API will generate code that accomplishes that task
import openai
openai.api_key = "YOUR_API_KEY"

description = "Create a Python script to sort a list of numbers in ascending order."
response = openai.Completion.create(
  engine="davinci-003",
  prompt=f"Code generation:\n{description}",
  max_tokens=100
)

code = response.choices[0].text.strip()
print(code)




########## Chat with bots ###########
#The OpenAI API can also be used for building chatbots. You can provide some context and a user’s message, and the API will generate a response
import openai
openai.api_key = "YOUR_API_KEY"

context = "You are chatting with a customer service representative."
message = "Hi, I have a problem with my account."
response = openai.Completion.create(
  engine="gpt-3.5-turbo",
  prompt=f"Chat:\n{context}\nUser: {message}\n",
  max_tokens=50
)

reply = response.choices[0].text.strip()
print(reply)



