import os
import numpy as np

from card_classifier.api import api

from config import Config


def convert_scores_to_color(output: dict, num_colors: int = 4) -> dict:
    """
    Assume each card has num_colors colors. Use the max score for all four unless more than one color scored > 0.25.
    In this case, assign colors in proportion
    """
    # Check if more than one color
    num_colors = len([k for k, v in output.items() if v > (1 / num_colors)])
    if num_colors > 1:
        normalization = num_colors / np.sum([score for score in output.values() if score > (1 / num_colors)])
        colors = {color: round(score * normalization) for color, score in output.items() if score > (1 / num_colors)}

    else:
        colors = {k: num_colors for k, v in output.items() if v == max(output.values())}

    return colors


def cc_api(default_card: str = None, uploaded_card: str = None):
    if default_card:
        # Vader has a weird extension
        ext = '.jpg' if default_card != 'vader' else '.jpeg'

        # If default card, get the preds for the all them extract the selected card
        input_path = os.path.join(Config.DATA_DIR, 'card_classifier', 'cc_samples')
        outputs = api(**{'version': Config.cc_version, 'model_type': Config.cc_model_type, 'input_path': input_path})
        output = outputs.get(os.path.join('images', default_card + ext))

        # With minified version, need to catch cross-OS complications
        if not output:
            output = outputs.get('images\\{}{}'.format(default_card, ext))

        # Parse output
        output = convert_scores_to_color(output)

    elif uploaded_card:
        # TODO: Implement
        return {}
    else:
        return {}

    return output
