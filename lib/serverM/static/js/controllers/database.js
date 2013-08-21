function DatabaseCtrl($scope, Module, $routeParams, Request, Message, Backend){
	var module = 'database';
	Module.init(module, '数据库管理');
	$scope.loaded = false;

	var section = Module.getSection();
	$scope.has_dbserver = false;
	$scope.mysql_supported = false;
	
	$scope.load = function(){
		Request.get('/query/service.mysqld', function(data){
			if (data['service.mysqld'] && data['service.mysqld'].status) $scope.mysql_supported = true;
			$scope.has_dbserver = $scope.mysql_supported;
			if ($scope.has_dbserver) {
				if (section) {
					if (section == 'mysqld' && $scope.mysql_supported)
						Module.setSection('mysqld');
					else
						Module.setSection($scope.mysql_supported ? 'mysql' : 'mysql');
				} else {
					Module.setSection($scope.mysql_supported ? 'mysql' : 'mysql');
				}
			}
			$scope.loaded = true;
			//$scope.loaddbs();
		});
	};
}