test = {   'name': 'q_adultmort',
    'points': 4,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(adultmort_2015.where('country', 'Bahamas').column('adultmort_m')[0], 0.204113, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(adultmort_2015.where('country', 'Bahamas').column('adultmort_f')[0], 0.122431, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
