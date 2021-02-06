test = {   'name': 'q_econ_join',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(all_mort_econ.where('country', 'Austria')['hlthexp'][0], 158327.79835698, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(all_mort_econ.where('country', 'Algeria')['childmort_m'][0], 0.0354724, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
