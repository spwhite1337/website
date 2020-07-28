import os
from unittest import TestCase

from presidents_speeches.api import api as ps_api
from card_classifier.api import api as cc_api
from sports_bettors.api import api as sb_api


from backend.config import Config, logger


class TestApiCalls(TestCase):
    def test_presidents_speeches(self):
        logger.info('Testing Presidents Speeches')
        ps_input = {
            'query': "Fake News",
            'num_out': 3,
            'display_output': True
        }
        output = ps_api(**ps_input)

    def test_card_classifier(self):
        logger.info('Testing Card Classifier')
        cc_input = {
            'version': Config.cc_version,
            'model_type': Config.cc_model_type,
            'input_path': os.path.join(Config.DATA_DIR, 'card_classifier', 'cc_samples'),
            'display_output': True
        }
        logger.info('Input: {}'.format(cc_input))
        output = cc_api(**cc_input)

    def test_sports_bettors(self):
        logger.info('Testing Sports Bettors')
        sb_input = {
            'league': 'nfl',
            'random_effect': 'team',
            'feature_set': 'RushOnly',
            'inputs': {
                'RandomEffect': 'CHI',
                'rushingYards': 150,
                'rushingAttempts': 30
            },
            'display_output': True
        }
        output = sb_api(**sb_input)

        sb_input = {
            'league': 'college_football',
            'random_effect': 'team',
            'feature_set': 'RushOnly',
            'inputs': {
                'RandomEffect': 'Iowa',
                'rushingYards': 150,
                'rushingAttempts': 30
            },
            'display_output': True
        }
        output = sb_api(**sb_input)
