import json


class Provider:
    @staticmethod
    def convertir_json_a_dict(filename, bloque):
        with open(filename) as file:
            data = file.read()
            content = json.loads(data)
        return content[bloque]
