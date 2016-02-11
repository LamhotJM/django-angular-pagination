SignEasyApp.factory('getDomainPrefix', ['$location', function($location) {
	return function(api) {
		var apiUrl;
		var currentUrl = $location.$$absUrl;
		return 'http://localhost:8000/'
	};
}]);
