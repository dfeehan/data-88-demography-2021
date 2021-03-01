test = {   'name': 'q_tdbl_unpd_1990_r',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(unpd_1990_r.where('area', 'Armenia').column('Tdbl')[0], -74.164313127947153, atol=.1)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(unpd_1990_r.where('area', 'Zimbabwe').column('Tdbl')[0], 27.500105825545823, atol=.1)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
