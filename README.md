# Instagram Caption Generator API using OpenAI

I have used the OpenAI GPT-3 model in this project for caption generation. I have created an API to access the OpenAI API to generate these captions.


1. Install the OpenAI library on the system and import the library.
2. You will need an OpenAI account with an API key to use the AI model.
3. The responses are generated by using the openai.Completion.create function.
4. The "engine" parameter is the model used for generating the captions. Here, the "text-davinci-002" model is used.
5. The "prompt" parameter is the instruction given to the model. The model generates the captions using the given list of keywords and also the given tone. The tone is the feeling that the caption intends to impart.
6. The "temperature" parameter is the variabiliaty in the generated captions. This allows the model to generate more arbitriary captions.
7. The "max_tokens" parameter is the maximum number of words in the captions.
8. The "top_p" parameter instructs the model to return the captions with the probability of 1.
9. The "frequency_penalty" parameter penalizes the model if it generates a word multiple times. Hence, repeatition of words is discouraged.
10. The "presence_penalty" paramter penalizes the model if the entered keyword exists in the generated captions. As we need the keywords in the captions, we set it to zero.
11. The "stop" parameter is the stopwords parameter. This removes the mentioned strings from the generated captions.
12. The hashtagsAndTone() function recieves the number of keywords, the keywords, and the tone for the caption to be generated.
13. To test the program, run the hashtagsAndTone() function and enter the keywords and the tone. Store the returned values in separate variables (keywords and tone) and pass them to the generateTheCaption() function. 
14. Voila! Now you can get AI generated instagram captions by simply providing keywords for the keywords you need.
