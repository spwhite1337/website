import json

from sports_bettors.api import api


def _parse_inputs(inputs: dict) -> dict:
    # Required fields
    league = {'College Football': 'college_football', 'NFL': 'nfl'}.get(inputs['league'])
    required = {
        'league': league,
        'random_effect': inputs['random_effect'],
        'feature_set': inputs['feature_set']
    }

    # Feature values for conditions (must include RandomEffect)
    options = [json.loads(input_) for input_ in inputs.getlist('inputs[]')]
    options = {item['name']: item['value'] for item in options}

    required['inputs'] = {k: float(v) for k, v in options.items() if k != 'RandomEffect'}
    required['inputs'].update({'RandomEffect': options['RandomEffect']})

    return required


def _parse_outputs(output: dict) -> dict:
    """
    We are fixing the random effect and feature set, so only need the response key of sb-output
    """
    return {k[2]: v for k, v in output.items()}


def sb_api(inputs: dict):
    # Parse inputs
    inputs = _parse_inputs(inputs)

    # Get betting probabilities
    output = api(**inputs)

    return _parse_outputs(output)
