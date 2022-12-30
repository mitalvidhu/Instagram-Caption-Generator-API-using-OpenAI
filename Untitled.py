#!/usr/bin/env python
# coding: utf-8

# In[50]:


import os
import openai

def generateTheCaption(keywords, tone):
    openai.api_key = "Your-OpenAI-API-Key"

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Catchy instagram captions on \"{keywords}\" in a {tone} tone.",
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
    )
    if len(response.choices) > 0:
        response = response.choices[0]
        return response.text.strip().replace("AI: ", "").strip()
    return "\n"
def hashtagsAndTone():
    print('How many keywords?')
    n = int(input())
    keywords = []
    for i in range(n):
        keywords.append(input())
    print('What is the tone?')
    tone = input()
    return ",".join(keywords), tone


# In[51]:


keywords, tone = hashtagsAndTone()
generateTheCaption(keywords, tone)


# In[52]:


keywords, tone = hashtagsAndTone()
generateTheCaption(keywords, tone)


# In[55]:


keywords, tone = hashtagsAndTone()
generateTheCaption(keywords, tone)


# In[56]:


keywords, tone = hashtagsAndTone()
generateTheCaption(keywords, tone)

