import os
from unittest import TestCase

from process_gambling.bets import bets as pg_api


from config import Config, logger


class TestApiCalls(TestCase):


    def test_sports_bettors(self):
        logger.info('Testing Sports Bettors')
        output = pg_api()
        logger.info(output)

