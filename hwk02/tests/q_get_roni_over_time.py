test = {   'name': 'q_get_roni_over_time',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> np.all(ug_roni.column('area') == 'Uganda')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.min(ug_roni.column('period')) == 1955\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.max(ug_roni.column('period')) == 2015\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
