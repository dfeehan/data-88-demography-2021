test = {   'name': 'q_county_pop_rank',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> np.isclose(county_pop_rank.sort('fips').column('pop_rank').item(3), 1703)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
