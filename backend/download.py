import os
import re
import argparse

from config import Config, logger


def download(windows: bool = False, dryrun: bool = False):
    base = 'aws s3 sync '
    dryrun_arg = ' --dryrun'
    results_sync = '{} {}'.format(Config.CLOUD_RESULTS, Config.RESULTS_DIR)
    data_sync = '{} {}'.format(Config.CLOUD_DATA, Config.DATA_DIR)

    logger.info('Data for Sports Bettors')
    # Select files
    include_flag = " --exclude '*' --include '*df_curated.csv'"
    include_flag = re.sub("'", '', include_flag) if windows else include_flag

    # Run
    sb_sync = base + data_sync + include_flag
    sb_sync += dryrun_arg if dryrun else ''
    logger.info(sb_sync)
    os.system(sb_sync)

    logger.info('Results for Sports Bettors')
    # Select files
    include_flag = " --exclude '*' --include '*predictor_set_{}.pkl'".format(Config.sb_version)
    include_flag = re.sub("'", '', include_flag) if windows else include_flag

    # Run
    sb_sync = base + results_sync + include_flag
    sb_sync += dryrun_arg if dryrun else ''
    logger.info(sb_sync)
    os.system(sb_sync)

    logger.info('Data for Presidents Speeches')
    # Include
    include_flag = " --exclude '*' --include '*corpus.pkl' --include '*dictionary.dict' "
    include_flag = re.sub("'", "", include_flag) if windows else include_flag

    # Run
    ps_sync = base + data_sync + include_flag
    ps_sync += dryrun_arg if dryrun else ''
    logger.info(ps_sync)
    os.system(ps_sync)

    logger.info('Results for Presidents Speeches')
    include_flag = " --exclude '*' --include 'presidents_speeches/*'"
    include_flag = re.sub("'", "", include_flag) if windows else include_flag
    ps_sync = base + results_sync + include_flag
    ps_sync += dryrun_arg if dryrun else ''
    logger.info(ps_sync)
    os.system(ps_sync)

    logger.info('Data for Card Classifier')
    include_flag = " --exclude '*' --include 'card_classifier/cc_samples/*.jpg'"
    include_flag = re.sub("'", "", include_flag) if windows else include_flag
    cc_sync = base + data_sync + include_flag
    cc_sync += dryrun_arg if dryrun else ''
    logger.info(cc_sync)
    os.system(cc_sync)

    logger.info('Results for Card Classifier')
    include_flag = " --exclude '*' --include 'card_classifier/{}/{}/*'".format(Config.cc_model_type, Config.cc_version)
    include_flag = re.sub("'", "", include_flag) if windows else include_flag
    cc_sync = base + results_sync + include_flag
    cc_sync += dryrun_arg if dryrun else ''
    logger.info(cc_sync)
    os.system(cc_sync)

    logger.info('Data for Wedding')
    include_flag = " --exclude '*' --include 'wedding/*.csv'"
    include_flag = re.sub("'", "", include_flag) if windows else include_flag
    wd_sync = base + data_sync + include_flag
    wd_sync += dryrun_arg if dryrun else ''
    logger.info(wd_sync)
    os.system(wd_sync)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--windows', action='store_true')
    parser.add_argument('--dryrun', action='store_true')
    args = parser.parse_args()
    download(args.windows, args.dryrun)
