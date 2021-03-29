test = {   'name': 'q_imr',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> np.isclose(in_migrants.where('fips', 1017).column('imr').item(0), 0.027113754121526144, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
