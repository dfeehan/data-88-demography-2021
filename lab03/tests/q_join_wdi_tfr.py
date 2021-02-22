test = {   'name': 'q_join_wdi_tfr',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Austria'))['pctf_primary'][0], 48.5654, atol=.1)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Azerbaijan'))['gdp'][0], 7496.29, atol=.1)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
