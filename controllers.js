var fozziesovApp = angular.module('fozziesovApp', []);

fozziesovApp.controller('BattleCtrl', function($scope) {
    $scope.battles = [
    {   'sysname': 'GE-8JV',
        'structname': 'Station',
        'corps':  [{'name': 'TEST Alliance Please Ignore', 'num': 584},
                   {'name': 'Brave Collective', 'num': 947} 
                  ],
        'events': [{'text': 'Cyno in SV-5'},
                   {'text': 'Brave fleet moving to SV-5'}
                   ],
        'system':  {'name': 'GE-8JV',
                    'corps': [{'name': 'TEST Alliance Please Ignore', 'num': 84},
                              {'name': 'Brave Collective', 'num': 124} 
                              ],
                    'events': [{'time': '21:43', 'text': 'dscan paste'},
                               {'time': '21:38', 'text': 'dscan paste'},
                               {'time': '20:23', 'text': 'dscan paste'}
                               ]
                   }
        }];
    $scope.systems = [
           {'name': 'GE-8JV',
            'corps': [{'name': 'TEST Alliance Please Ignore', 'num': 84},
                      {'name': 'Brave Collective', 'num': 124} 
                      ],
            'events': [{'time': '21:43', 'text': 'dscan paste'},
                       {'time': '21:38', 'text': 'dscan paste'},
                       {'time': '20:23', 'text': 'dscan paste'}
                       ]
            }
        ];
});
