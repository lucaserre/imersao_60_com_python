api_response = {
    'status': 200,
    'erro' : False,
    'payload': {
        'id_transacao': 'TX-999',
        'cliente_detalhes': {
            'nome': 'Lucas',
            'contatos': {
                'email': 'lucas@email.com',
                'whatsapp': '31999999999'
            }
        }
    }
}

print(api_response['payload']['erro']['cliente_detalhes']['nome']['contatos']['email'] )


