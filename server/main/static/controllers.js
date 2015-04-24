var fozziesovApp = angular.module('fozziesovApp', []);

fozziesovApp.controller('StratopCtrl', function($scope, $http, $interval) {
   $interval(function(){
       $http.post('').success(function(data) {
           $scope.stratop = data;
       }); 
   }, 1000);
});
