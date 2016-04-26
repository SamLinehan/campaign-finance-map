angular.module('cf-map')
  .controller("HomeController", HomeController);

  HomeController.$inject = ['$scope'];

  function HomeController() {
    console.log("Home Controller");
  }
