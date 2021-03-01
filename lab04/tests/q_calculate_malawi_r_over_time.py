test = {   'name': 'q_calculate_malawi_r_over_time',
    'points': 5,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(np.min(country_r['r']),0.2683012127931062, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(np.max(country_r['r']),6.2869285616472936, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(country_r.where('period', 1980).column('r')[0],2.9097781948165324, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
