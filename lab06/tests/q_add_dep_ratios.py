test = {   'name': 'q_add_dep_ratios',
    'points': 6,
    'suites': [   {   'cases': [   {'code': ">>> np.isclose(india_proj_withdr.where('iteration', 9).column('total_dr').item(0), 79.60620021042531, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(india_proj_withdr.where('iteration', 0).column('child_dr').item(0), 73.41500817335282, atol=.01)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(india_proj_withdr.where('iteration', 8).column('old_dr').item(0), 5.97299451216864, atol=.01)\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
