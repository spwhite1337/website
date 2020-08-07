# backend

## Procedure

- Python 3.5
- `pip install -e .`
- `aws configure`
    - Enter keys from `s3://scott-p-white` bucket
- `python download.py`

## Unittests

- `cd tests`
- `python -m unittest`

Output:

```
>python -m unittest
2020-08-06 22:48:41.789000: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'cudart64_101.dll'; dlerror: cudart64_101.dll not found
2020-08-06 22:48:41.820256: I tensorflow/stream_executor/cuda/cudart_stub.cc:29] Ignore above cudart dlerror if you do not have a GPU set up on your machine.
2020-08-06 22:49:33 INFO     Testing Card Classifier
2020-08-06 22:49:33 INFO     Input: {'version': 'v1', 'model_type': 'VGG', 'input_path': 'c:\\users\\spwhi\\codebase\\website\\backend\\data\\card_classifier\\cc_samples', 'display_output': True}
2020-08-06 22:49:38.815168: W tensorflow/stream_executor/platform/default/dso_loader.cc:59] Could not load dynamic library 'nvcuda.dll'; dlerror: nvcuda.dll not found
2020-08-06 22:49:38.815340: W tensorflow/stream_executor/cuda/cuda_driver.cc:312] failed call to cuInit: UNKNOWN ERROR (303)
2020-08-06 22:49:38.819735: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:169] retrieving CUDA diagnostic information for host: DESKTOP-T8QK0RG
2020-08-06 22:49:38.820010: I tensorflow/stream_executor/cuda/cuda_diagnostics.cc:176] hostname: DESKTOP-T8QK0RG
2020-08-06 22:49:38.915858: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN)to use the following CPU instructions in performance-critical operations:  AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2020-08-06 22:49:41.072204: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x1e69fcfc950 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-08-06 22:49:41.072345: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
Found 10 images belonging to 1 classes.
10/10 [==============================] - 1s 77ms/step
10/10 [==============================] - 1s 75ms/step
10/10 [==============================] - 1s 79ms/step
10/10 [==============================] - 1s 83ms/step
10/10 [==============================] - 1s 88ms/step
10/10 [==============================] - 1s 92ms/step
2020-08-06 22:50:31 INFO     Output:
{   'images\\balrog.jpg': {   'B': 0.5267415,
                              'G': 0.045847446,
                              'N': 0.25855398,
                              'R': 0.275528,
                              'U': 0.0010831058,
                              'W': 0.024983019},
    'images\\galadriel.jpg': {   'B': 0.015787214,
                                 'G': 0.26406306,
                                 'N': 0.9815355,
                                 'R': 0.017555892,
                                 'U': 0.002957821,
                                 'W': 0.06654954},
    'images\\javert.jpg': {   'B': 0.4530452,
                              'G': 0.15237981,
                              'N': 0.056774497,
                              'R': 0.04962504,
                              'U': 0.03554538,
                              'W': 0.06373078},
    'images\\jean.jpg': {   'B': 0.30917722,
                            'G': 0.13248375,
                            'N': 0.3642934,
                            'R': 0.32482594,
                            'U': 0.0010573268,
                            'W': 0.025173396},
    'images\\link.jpg': {   'B': 0.3224331,
                            'G': 0.490238,
                            'N': 0.93159884,
                            'R': 0.010537595,
                            'U': 0.0024097264,
                            'W': 0.89140755},
    'images\\mary.jpg': {   'B': 0.9783472,
                            'G': 0.10777831,
                            'N': 0.00032165647,
                            'R': 0.056817085,
                            'U': 0.019179344,
                            'W': 0.032522142},
    'images\\napolean.jpg': {   'B': 0.77337265,
                                'G': 0.10725021,
                                'N': 0.051620066,
                                'R': 0.12879491,
                                'U': 0.009865522,
                                'W': 0.03924814},
    'images\\sauron.jpg': {   'B': 6.172084e-10,
                              'G': 1.6971251e-05,
                              'N': 4.5033044e-09,
                              'R': 0.00040400028,
                              'U': 0.0009454489,
                              'W': 0.99986947},
    'images\\tolstoy.jpg': {   'B': 0.62263674,
                               'G': 0.14649346,
                               'N': 0.09789431,
                               'R': 0.014052153,
                               'U': 0.008130014,
                               'W': 0.024071217},
    'images\\vader.jpeg': {   'B': 0.14316884,
                              'G': 0.4074848,
                              'N': 0.39106447,
                              'R': 0.08809587,
                              'U': 0.0012653768,
                              'W': 0.010184258}}
.2020-08-06 22:50:31 INFO     Testing Presidents Speeches
2020-08-06 22:50:31 INFO     Load Corpus
2020-08-06 22:50:35 INFO     Loading Dictionary, Similarity Index
2020-08-06 22:50:35 INFO     loading Dictionary object from c:\users\spwhi\codebase\website\backend\data\presidents_speeches\curated\dictionary.dict
2020-08-06 22:50:35 INFO     loaded c:\users\spwhi\codebase\website\backend\data\presidents_speeches\curated\dictionary.dict
2020-08-06 22:50:35 INFO     loading MatrixSimilarity object from c:\users\spwhi\codebase\website\backend\results\presidents_speeches\similarities.index
2020-08-06 22:50:35 INFO     loaded c:\users\spwhi\codebase\website\backend\results\presidents_speeches\similarities.index
2020-08-06 22:50:35 INFO     Load models
2020-08-06 22:50:35 INFO     loading TfidfModel object from c:\users\spwhi\codebase\website\backend\results\presidents_speeches\tfidf.model
2020-08-06 22:50:35 INFO     loaded c:\users\spwhi\codebase\website\backend\results\presidents_speeches\tfidf.model
2020-08-06 22:50:35 INFO     loading LsiModel object from c:\users\spwhi\codebase\website\backend\results\presidents_speeches\lsi.model
2020-08-06 22:50:35 INFO     loading id2word recursively from c:\users\spwhi\codebase\website\backend\results\presidents_speeches\lsi.model.id2word.* with mmap=None
2020-08-06 22:50:35 INFO     setting ignored attribute dispatcher to None
2020-08-06 22:50:35 INFO     setting ignored attribute projection to None
2020-08-06 22:50:35 INFO     loaded c:\users\spwhi\codebase\website\backend\results\presidents_speeches\lsi.model
2020-08-06 22:50:35 INFO     loading LsiModel object from c:\users\spwhi\codebase\website\backend\results\presidents_speeches\lsi.model.projection
2020-08-06 22:50:35 INFO     loaded c:\users\spwhi\codebase\website\backend\results\presidents_speeches\lsi.model.projection
2020-08-06 22:50:35 INFO     Mapping query to LSI Space
2020-08-06 22:50:35 INFO     Comparing to Corpus
2020-08-06 22:50:36 INFO     Output:
{   'Fake News': {   'presidents': ['trump', 'clinton', 'obama'],
                     'presidents_sim': [   3.991385757923126,
                                           3.9502575993537903,
                                           3.949316680431366],
                     'speeches': [   'https://millercenter.org/the-presidency/presidential-speeches/february-23-2018-remarks-conservative-political-action',
                                     'https://millercenter.org/the-presidency/presidential-speeches/july-24-2017-speech-boy-scout-jamboree',
                                     'https://millercenter.org/the-presidency/presidential-speeches/october-6-1996-presidential-debate-senator-bob-dole'],
                     'speeches_sim': [   3.976735532283783, 3.9579113721847534,
                                         3.949946939945221]}}
.2020-08-06 22:50:36 INFO     Testing Sports Bettors
2020-08-06 22:50:36 INFO     Loading predictor set for nfl
2020-08-06 22:50:36 INFO     Input: {'RandomEffect': 'CHI', 'rushingYards': 150, 'rushingAttempts': 30}
2020-08-06 22:50:36 INFO     Output:
{   ('team', 'RushOnly', 'LossMargin'): {   'mu': {   'lb': 11.350517125376513,
                                                      'mean': 11.733497675568586,
                                                      'ub': 12.116478225760659},
                                            'sigma': {   'lb': 9.020737754734782,
                                                         'mean': 9.076146979627058,
                                                         'ub': 9.131556204519335}},
    ('team', 'RushOnly', 'Margin'): {   'mu': {   'lb': 0.5600728219656743,
                                                  'mean': 0.9905954055184588,
                                                  'ub': 1.4211179890712433},
                                        'sigma': {   'lb': 12.495524454026041,
                                                     'mean': 12.546819488200619,
                                                     'ub': 12.598114522375196}},
    ('team', 'RushOnly', 'TotalPoints'): {   'mu': {   'lb': 39.21352143166286,
                                                       'mean': 39.66705760670118,
                                                       'ub': 40.120593781739494},
                                             'sigma': {   'lb': 14.040654969318101,
                                                          'mean': 14.098706861493424,
                                                          'ub': 14.156758753668747}},
    ('team', 'RushOnly', 'Win'): {   'mu': {   'lb': 0.041583859378134094,
                                               'mean': 0.12003473066032205,
                                               'ub': 0.19848560194251003}},
    ('team', 'RushOnly', 'WinMargin'): {   'mu': {   'lb': 12.3450007536196,
                                                     'mean': 12.711522237883655,
                                                     'ub': 13.07804372214771},
                                           'sigma': {   'lb': 9.003596621370459,
                                                        'mean': 9.058188389559072,
                                                        'ub': 9.112780157747686}}}
2020-08-06 22:50:36 INFO     Loading predictor set for college_football
2020-08-06 22:50:36 INFO     Input: {'RandomEffect': 'Iowa', 'rushingYards': 150, 'rushingAttempts': 30}
2020-08-06 22:50:36 INFO     Output:
{   ('team', 'RushOnly', 'LossMargin'): {   'mu': {   'lb': 5.203407115684713,
                                                      'mean': 6.693706556567932,
                                                      'ub': 8.184005997451152},
                                            'sigma': {   'lb': 12.933691310049893,
                                                         'mean': 13.018212804017745,
                                                         'ub': 13.102734297985597}},
    ('team', 'RushOnly', 'Margin'): {   'mu': {   'lb': 6.585329165536013,
                                                  'mean': 7.641162796263397,
                                                  'ub': 8.696996426990781},
                                        'sigma': {   'lb': 18.085038403813193,
                                                     'mean': 18.171557216983697,
                                                     'ub': 18.2580760301542}},
    ('team', 'RushOnly', 'TotalPoints'): {   'mu': {   'lb': 46.89018052371675,
                                                       'mean': 47.898364227578945,
                                                       'ub': 48.90654793144114},
                                             'sigma': {   'lb': 16.932600687085372,
                                                          'mean': 17.003502059890415,
                                                          'ub': 17.07440343269546}},
    ('team', 'RushOnly', 'Win'): {   'mu': {   'lb': 0.2877182200285193,
                                               'mean': 0.43064431853860385,
                                               'ub': 0.5735704170486884}},
    ('team', 'RushOnly', 'WinMargin'): {   'mu': {   'lb': 17.350635208395776,
                                                     'mean': 18.049121264808306,
                                                     'ub': 18.747607321220833},
                                           'sigma': {   'lb': 12.933624296832694,
                                                        'mean': 13.012824812353006,
                                                        'ub': 13.09202532787332}}}
.
----------------------------------------------------------------------
Ran 3 tests in 62.951s

OK
```