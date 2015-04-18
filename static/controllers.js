var fozziesovApp = angular.module('fozziesovApp', []);

fozziesovApp.controller('StratopCtrl', function($scope, $http, $interval) {
   $http.post('/test').success(function(data) {
       $scope.stratop = data;
   }); 
   $interval(function(){
       $http.post('/test').success(function(data) {
           $scope.stratop = data;
       }); 
   }, 1000);
});
