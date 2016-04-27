angular.module('cf-map')
  .controller("HomeController", HomeController);

  HomeController.$inject = ['$scope', 'd3Service'];

  function HomeController($scope, d3Service) {
    console.log("Home Controller");
    d3Service.testFunction()
      .then(function(data) {
        $scope.data = data;
      })
  }
