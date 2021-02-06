test = {   'name': 'q_adult_join',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(all_mort.where('country', 'Aruba').select('e0_f', 'adultmort_m')[1][0], 0.120311, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(all_mort.where('country', 'Aruba').select('e0_f', 'adultmort_m')[0][0], 77.7563, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
