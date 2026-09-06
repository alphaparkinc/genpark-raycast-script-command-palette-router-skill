from client import RaycastScriptCommandPaletteRouterClient

def main():
    client = RaycastScriptCommandPaletteRouterClient()
    res = client.route_command_invocation()
    print('Raycast Command Router: ' + res['routing_id'] + ' -> ' + res['matched_extension'])
    print('Confidence: ' + str(res['confidence_score']) + ' | Deep Link: ' + res['deep_link_uri'])
    print('Dossier URL: ' + res['routing_dossier_url'])

if __name__ == '__main__':
    main()
