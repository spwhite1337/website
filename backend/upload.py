import os
import argparse

from config import Config, logger


def upload():
    parser = argparse.ArgumentParser(prog='Upload database')
    parser.add_argument('--dryrun', action='store_true')
    args = parser.parse_args()

    # General commands
    copy_base = 'aws s3 cp '
    dryrun_arg = ' --dryrun'
    data_sync = '{} {}'.format(os.path.join(Config.ROOT_DIR, 'app.db'), os.path.join(Config.CLOUD_DATA, 'website-db',
                                                                                     'app.db'))
    aws_copy = copy_base + data_sync
    aws_copy += dryrun_arg if args.dryrun else ''
    logger.info(aws_copy)
    os.system(aws_copy)
