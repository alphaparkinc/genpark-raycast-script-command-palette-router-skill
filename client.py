class RaycastScriptCommandPaletteRouterClient:
    def route_command_invocation(self, query_string='create ticket PR #104', hotkey_chord='cmd+shift+p'):
        return {
            'routing_id': 'cmd_rot_9918',
            'query': query_string,
            'matched_extension': 'linear-issue-creator',
            'confidence_score': 0.96,
            'extracted_arguments': {'action': 'create_issue', 'reference': 'PR #104'},
            'keyboard_chord_invoked': hotkey_chord,
            'deep_link_uri': 'raycast://extensions/linear/create-issue?title=PR%20%23104',
            'routing_dossier_url': 'https://productivity.developer.genpark.ai/raycast/cmd_rot_9918.json'
        }
