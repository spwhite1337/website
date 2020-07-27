import os
from card_classifier.api import api

from config import Config


def cc_api(default_card: str = None, uploaded_card: str = None):
    if default_card:
        # If default card, get the preds for the all them extract the selected card
        input_path = os.path.join(Config.DATA_DIR, 'card_classifier', 'cc_samples')
        outputs = api(**{'version': Config.cc_version, 'model_type': Config.cc_model_type, 'input_path': input_path})
        output = outputs.get(os.path.join('images', default_card + '.jpg'))

        # Check if more than one color is above 50%
        num_colors = len([k for k, v in output.items() if v > 0.5])
        if num_colors > 1:
            colors = [k for k, v in output.items() if v > 0.5]
            normalized_score = 0.
        else:
            colors = [k for k, v in output.items() if v == max(output.values())]

        # Convert floats to strings for json
        output = colors

    elif uploaded_card:
        # TODO: Implement
        return {}
    else:
        return {}

    return output
