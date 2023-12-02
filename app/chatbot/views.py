from django.shortcuts import render
from django.http import HttpResponse
import os
from langchain.llms import Replicate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import joblib

# Cargar el modelo si ya existe, o crearlo y guardarlo

os.environ["REPLICATE_API_TOKEN"] = "r8_Vjc3lXrrj0wXA8KMEKb9L3UHYaHXXvB229IQ1"

prompt = PromptTemplate(input_variables=["data_text"],
                        template=""" I would give you data from a object json and you should,
make a detalied guess of what's happening on the data (Is an json about public officials sanctioned):

Example:
"It seems like you've provided information about a case involving a public servant from the Fiscalia General del Estado (FGE). The details include the individual's name (Andres Reyes Enriquez), position (Fiscal del Ministerio Publico, adscrito a la Fiscalia de la Mujer), and the sanction imposed on them.

Here's a summary of the information:

ID: b411f02b-5ea7-489e-93e5-9eca24d090f6
Date of Capture: 2022-05-06
Case File: CA/012/2022
Institution: Fiscalia General del Estado (FGE)
Public Servant Sanctioned:
Full Name: Andres Reyes Enriquez
Position: Fiscal del Ministerio Publico, adscrito a la Fiscalia de la Mujer
Level: Datos no proporcionados (Data not provided)
Sanctioning Authority: Datos no proporcionados (Data not provided)
Type of Offense:
Code: OTRO
Value: OTRO
Type of Sanction:
Code: I
Value: INHABILITADO (Disqualified/Ineligible)
Cause/Motive of Actions: Datos no proporcionados (Data not provided)
Resolution:
URL: Datos no proporcionados (Data not provided)
Date: 2022-01-12
Fine:
Amount: 0 MXN (Mexican Peso)
Disqualification:
Term: 3 MESES (3 months)
Start Date: 2022-02-15
End Date: 2022-05-15"

Data:
{data_text}

Image Description:


""")

model_filename = "modelo_replicado.joblib"
if os.path.exists(model_filename):
    llm = joblib.load(model_filename)
else:
    llm = Replicate(
        model="meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        model_kwargs={"temperature": 0.75, "max_length": 5000, "top_p": 1},
    )
    joblib.dump(llm, model_filename)

def index(request):
    if request.method == 'POST':
        data_text = request.POST['data_text']

        # Utilizar el modelo para obtener la respuesta
        response_text = llm(prompt.format(data_text=data_text))

        return render(request, 'chat.html', {'data_text': data_text, 'response_text': response_text})
    else:
        return render(request, 'chat.html')
