test = {   'name': 'q_mac_tfr_join',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Argentina'))['mac'][0], 28.097, atol=.1)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(unpd_tfr_2015_econ.where('area', are.equal_to('Angola'))['tfr'][0], 5.95, atol=.1)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
