import json
import requests
from pdf_generator import generate_pdf

def doUFPdf(event, context):
    valorUF = requests.get(url = 'https://mindicador.cl/api/uf').json()['serie'][0]['valor']
    if generate_pdf(valorUF):
        return {
            'statusCode': 200,
            'body': 'Se ha creado el archivo con el precio de la UF.'
        }
    else:
        return {
            'statusCode': 500,
            'body': 'No fue posible crear el archivo solicitado.'
        }