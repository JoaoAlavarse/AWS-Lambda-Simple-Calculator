AWS-Lambda-Simple-Calculator

Este é um projeto simples que implementa uma calculadora em python utilizando a AWS Lambda

Link para teste da lambda: https://i6sk4vpjbcviseceejxsddzjti0toeep.lambda-url.us-east-2.on.aws/

Corpo esperado pela requisição:
{
    "oneValue": 10,
    "operation": "times",
    "anotherValue": 2
}

oneValue e another value precisam ser numéricos
operation precisa ser um texto e precisa ser um dos seguintes: plus, minus, divided, times

A resposta espera é um texto com o valor desejado. Partindo do esxemplo de corpo da requisição, o retorno seria: 20
