angular.module('cf-map', ['ui.router'])
  .directive('testDirective', ['d3Service', function() {
    return {
      template: '<img src="https://lh6.googleusercontent.com/-TlY7amsfzPs/T9ZgLXXK1cI/AAAAAAABK-c/Ki-inmeYNKk/w749-h794/AngularJS-Shield-large.png">'
    };
  }])
  .config(function($stateProvider, $urlRouterProvider) {
    
    $urlRouterProvider.otherwise("/home");

    $stateProvider.state("home", {
      templateUrl: "templates/home.html",
      controller: "HomeController",
      url: "/home"
    })
  })
