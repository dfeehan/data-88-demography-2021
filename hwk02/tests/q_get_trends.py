test = {   'name': 'q_get_trends',
    'points': 4,
    'suites': [   {   'cases': [   {'code': ">>> france_trends.where('period', 1985).column('area').item(0) == 'France'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(france_trends.where('period', 1985).column('tfr').item(0), 1.8653, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(france_trends.where('period', 1985).column('e').item(0), 78.7893, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(france_trends.where('period', 1985).column('child_mort').item(0), 0.01000451, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
