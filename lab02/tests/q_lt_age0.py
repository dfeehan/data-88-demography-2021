test = {   'name': 'q_lt_age0',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> lt_m_age0.num_rows == 201\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> lt_m_age0.where('area', are.equal_to('France')).column('age')[0] == 0\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> lt_m_age0.where('area', are.equal_to('France')).column('sex')[0] == 'male'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
