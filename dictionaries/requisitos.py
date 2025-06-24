data = [
    {"documento": "Documento: Cartera de Servicio al trabajador ", "requisitos": []},
    {"documento": "Documento: Solicitud Correo Electrónico ", "requisitos": []},
    {"documento": "Documento: Solicitud Declara Tabasco ", "requisitos": []},
    {
        "documento": "Documento: Solicitud Pagos Extemporaneos de días económicos ",
        "requisitos": [
            {
                "requisito": "Requisito: Copia del último talón de pago ",
                "documento_requisito": "ArchivoRequisitoSubido: Copia del último talón de pago ",
            },
            {"requisito": "Requisito: Copia de la CURP ", "documento_requisito": None},
            {
                "requisito": "Requisito: Identificación oficial vigente con fotografía ",
                "documento_requisito": None,
            },
            {
                "requisito": "Requisito: Constancia de situación fiscal ",
                "documento_requisito": None,
            },
            {
                "requisito": "Requisito: Carátula del contrato bancario ",
                "documento_requisito": None,
            },
        ],
    },
    {
        "documento": "Documento: Solicitud de Pagos Extemporaneos de Aguinaldo ",
        "requisitos": [
            {
                "requisito": "Requisito: Copia de identificación oficial ",
                "documento_requisito": None,
            },
            {
                "requisito": "Requisito: Constancia de situación fiscal ",
                "documento_requisito": None,
            },
            {
                "requisito": "Requisito: Estado de cuenta bancario vigente a nombre del suscrito ",
                "documento_requisito": None,
            },
        ],
    },
]


for documento in data:
    for k, v in documento.items():
        print(f'Key: {k} Value: {v}')
