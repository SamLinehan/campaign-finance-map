angular.module('cf-map')
  .factory('d3Service', d3Service);

  d3Service.$inject = ['$http'];

  function d3Service($http) {
    // var d3;
    console.log("Hello from d3Service");
    return {
      testFunction: function testFunction() {
        return $http.get('http://localhost:5000/candidates')
        .then(function(response) {
          console.log(response.data);
        })
      }
    }
  };
