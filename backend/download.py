import os
import re
import argparse

from backend.config import Config, logger


def download(windows: bool, dryrun: bool):
    # General commands
    sync_base = 'aws s3 sync '
    dryrun_arg = ' --dryrun'
    results_sync = '{} {}'.format(Config.CLOUD_RESULTS, Config.RESULTS_DIR)
    data_sync = '{} {}'.format(Config.CLOUD_DATA, Config.DATA_DIR)

    # Sync presidents (download lsi, tfidf models, similarities index, and corpus)
    logger.info('Syncing results for presidents-speeches')
    ps_include = " --exclude '*' --include 'presidents_speeches/lsi.model' " \
                 "--include 'presidents_speeches/lsi.model.projection' " \
                 "--include 'presidents_speeches/similarities.index' " \
                 "--include 'presidents_speeches/tfidf.model'"
    if windows:
        ps_include = re.sub("'", "", ps_include)
    ps_sync = sync_base + results_sync + ps_include
    ps_sync += dryrun_arg if dryrun else ''
    logger.info(ps_sync)
    os.system(ps_sync)

    logger.info('Syncing data for presidents-speeches')
    ps_include = " --exclude '*' --include 'presidents_speeches/curated/corpus.pkl'" \
                 " --include 'presidents_speeches/curated/dictionary.dict'"
    if windows:
        ps_include = re.sub("'", "", ps_include)
    ps_sync = sync_base + data_sync + ps_include
    ps_sync += dryrun_arg if dryrun else ''
    logger.info(ps_sync)
    os.system(ps_sync)

    # Sync card-classifier (download specified model along with samples for unittest)
    logger.info('Syncing results for card-classifier')
    cc_include = " --exclude '*' --include 'card_classifier/{0}/{1}/*' --exclude '*.pdf'".format(Config.cc_model_type,
                                                                                                 Config.cc_version)
    if windows:
        cc_include = re.sub("'", "", cc_include)
    cc_sync = sync_base + results_sync + cc_include
    cc_sync += dryrun_arg if dryrun else ''
    logger.info(cc_sync)
    os.system(cc_sync)

    cc_include = " --exclude '*' --include 'card_classifier/cc_samples/*'"
    if windows:
        cc_include = re.sub("'", "", cc_include)
    cc_sync = sync_base + data_sync + cc_include
    cc_sync += dryrun_arg if dryrun else ''
    logger.info(cc_sync)
    os.system(cc_sync)

    # Sync sports-bettors (only download predictor_sets for version)
    logger.info('Syncing results for sports-bettors')
    sb_include = " --exclude '*' --include 'sports_bettors/*predictor_set_{}.pkl'".format(Config.sb_version)
    if windows:
        sb_include = re.sub("'", "", sb_include)
    sb_sync = sync_base + results_sync + sb_include
    sb_sync += dryrun_arg if dryrun else ''
    logger.info(sb_sync)
    os.system(sb_sync)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Download results')
    parser.add_argument('--windows', action='store_true')
    parser.add_argument('--dryrun', action='store_true')
    args = parser.parse_args()
    download(args.windows, args.dryrun)
