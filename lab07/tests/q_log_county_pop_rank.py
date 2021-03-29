test = {   'name': 'q_log_county_pop_rank',
    'points': 4,
    'suites': [   {   'cases': [{'code': ">>> np.isclose(county_pop_rank.where('pop_rank', 100).column('minus_log_rank').item(0), -4.60517, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
