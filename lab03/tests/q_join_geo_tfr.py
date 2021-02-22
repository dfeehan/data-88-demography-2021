test = {   'name': 'q_join_geo_tfr',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> unpd_tfr_2015.where('area', are.equal_to('Austria'))['subregion_name'][0] == 'Western Europe'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> unpd_tfr_2015.where('area', are.equal_to('Algeria'))['income_level'][0] == 'middle'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
