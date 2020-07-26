from presidents_speeches.api import api


def ps_api(query: str):
    output = api(**{'query': query, 'num_out': 3, 'display_output': False})
    # Return most similar president
    return output[query]['presidents'][0]
