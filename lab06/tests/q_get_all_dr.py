test = {   'name': 'q_get_all_dr',
    'points': 7,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(us_all_dr.where('period', 1990).column('old_dr').item(0), 22.79315196501489, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(us_all_dr.where('period', 1970).column('child_dr').item(0), 44.02131059598877, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(us_all_dr.where('period', 1955).column('total_dr').item(0), 61.25062886091597, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
