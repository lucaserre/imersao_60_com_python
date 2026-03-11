import json

configuracao = {

        "nome_robo" : "Cobradeiro_v1",
        "versao": 1.5,

        "hora_cobranca": {
        
        "manha" : [9,10,11],
        "tarde" : [13,14,15],
        "noite" : [20,21]

        },

        "dia_cobranca" : ["segunda", "terca", "quarta", "quinta", "sexta"]

        

}

with open("config.json", "w") as cobradeiro_config:
    json.dump(configuracao, cobradeiro_config, indent=4 )


