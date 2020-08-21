from presidents_speeches.api import api


def ps_api(query: str, num_out: int = 3):
    output = api(**{'query': query, 'num_out': num_out, 'display_output': False})
    return output[query]
