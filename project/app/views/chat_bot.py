# from django.shortcuts import render,redirect
# import random
# from app.models import Patient,Appointment,Department
# from django.contrib import messages
# import openai
# openai.api_key = "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"

# def get_gpt_response(prompt, max_tokens=200):

#   prompt = f"Answer the following question: {prompt}\nAnswer:"

#   response = openai.Completion.create(
#   engine="davinci",
#   prompt=prompt,
#   max_tokens=100,
#   n=1,
#   stop="\n", # Set a stop sequence here
#   temperature=0.7,
#   ) 
  
#   return response.choices[0].text
        


# def home(request):
 
 
#     prompt = ""

#     # while(prompt != "end"):

#     #     prompt = input("Type End to exit.\nEnter Text: ")
#     response = get_gpt_response(prompt)
#     context={
#        'response':response,
#     }
#     # print(response)

        

#     return render(request,'home/index.html',context)
