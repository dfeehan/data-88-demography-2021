test = {   'name': 'q_out_migrants_omr',
    'points': 2,
    'suites': [   {   'cases': [{'code': ">>> np.isclose(out_migrants.where('fips', 1017).column('omr').item(0), 0.0283208, atol=.001)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
