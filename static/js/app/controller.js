SignEasyApp.controller('dummyController', [function() {
	return;
}]);

SignEasyApp.controller('StateListControl', ['$scope', '$http', 'getDomainPrefix', function($scope, $http, getDomainPrefix) {

	$scope.initializeList = function() {
		// Populate the list values
		$scope.pageNum=1;
		$scope.pageSize = 5;
		$scope.loadPage();
		// $scope.currentPage = $scope.pageNum;
	};

	$scope.loadPage = function(){
		$http.get(getDomainPrefix()+'state/?pageNum='+ $scope.pageNum+'&pageSize='+$scope.pageSize).
		success(function(data, status, headers, config) {
			$scope.stateList = data.statesList;
			$scope.totalStates = data.totalStates;
	        $scope.currentBegin = ($scope.pageNum - 1) * $scope.pageSize + 1;
	        $scope.currentEnd = Math.min($scope.currentBegin + $scope.pageSize - 1, $scope.totalStates);

	        totalPages = Math.ceil($scope.totalStates/$scope.pageSize);

			$scope.maxSize = 5;
			$scope.itemsPerPage = $scope.pageSize;
			$scope.totalItems = $scope.totalStates;
			// $scope.bigCurrentPage = 1;
		}).
		error(function(data, status, headers, config) {
			// log error
			console.log("error fetching states list");
		});

		// Make the list element visible
		$('#stateList').removeProp('hidden');
	}

	$scope.resetPageSize=function(){
		$scope.pageNum=1;
		$scope.loadPage();
	}

}]);
