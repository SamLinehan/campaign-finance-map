angular.module('cf-map', ['ui.router'])
  .config(function($stateProvider, $urlRouterProvider) {
    console.log("Angulahhhh");

    $urlRouterProvider.otherwise("/home");

    $stateProvider.state("home", {
      templateUrl: "templates/home.html",
      controller: "HomeController",
      url: "/home"
    })
  })
