import os
import itertools
import numpy as np

from card_classifier.api import api

from config import Config


def convert_scores_to_color(output: dict, num_colors: int = 4) -> list:
    """
    Assume each card has num_colors colors. Use the max score for all four unless more than one color scored > 0.25.
    In this case, assign colors in proportion
    """
    # Check if more than one color
    num_colors_in_card = len([k for k, v in output.items() if v > (1 / num_colors)])
    if num_colors_in_card > 1:
        # Norm-const is the num_colors / (sum of scores above (1 / num_colors))
        # Normalized score is the "fraction of total score from value cards that this card comprises"
        normalization = num_colors / np.sum([score for score in output.values() if score > 0.5])
        colors = {color: round(score * normalization) for color, score in output.items() if score > 0.5}

    else:
        colors = {k: num_colors for k, v in output.items() if v == max(output.values())}

    # Convert dict of color: num to list of each color
    colors = list(itertools.chain.from_iterable([[k] * v for k, v in colors.items()]))

    # Fill with N
    colors += ['N'] * (num_colors - len(colors))

    return sorted(colors)


def cc_api(default_card: str = None, uploaded_card: str = None):
    if default_card:
        # If default card, get the preds for the all them extract the selected card
        input_path = os.path.join(Config.DATA_DIR, 'card_classifier', 'cc_samples')
        outputs = api(**{'version': Config.cc_version, 'model_type': Config.cc_model_type, 'input_path': input_path})
        output = outputs.get(os.path.join('images', default_card))

        # With minified version, need to catch cross-OS complications
        if not output:
            output = outputs.get('images\\{}'.format(default_card))

        # Parse output
        output = convert_scores_to_color(output)

    elif uploaded_card:
        # TODO: Implement
        return {}
    else:
        return {}

    return output
