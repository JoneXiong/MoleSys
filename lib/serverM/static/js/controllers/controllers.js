function LoginCtrl($scope, $rootScope, $location, Module, Message, Request){
	var module = 'login';
	Module.init(module, '登录');
	$scope.loginText = '登录';
	$scope.showForgetPwdMsg = false;
	$scope.showLoginForm = true;
	$scope.username = '';
	$scope.password = '';

	var password_strength = function(pwd) {
		var strongRegex = new RegExp("^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*\\W).*$", "g");
		var mediumRegex = new RegExp("^(?=.{7,})(((?=.*[A-Z])(?=.*[a-z]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[a-z])(?=.*[0-9]))).*$", "g");
		var enoughRegex = new RegExp("(?=.{6,}).*", "g");
		if (false == enoughRegex.test(pwd)) {
			return '无安全性可言';
		} else if (strongRegex.test(pwd)) {
			return '高';
		} else if (mediumRegex.test(pwd)) {
			return '一般';
		} else {
			return '低';
		}
	};

	$scope.login = function(rawpwd) {
		$scope.loginText = '登录中...';
		Request.post('/login', {
			username: $scope.username,
			password: rawpwd ? $scope.password : hex_md5($scope.password)
		}, function(data){
			if (data.code >= 0) {
				$scope.showLoginForm = false;
				var path = $rootScope.loginto ? $rootScope.loginto : '/main';
				if (data.code == 0) {
					$location.path(path);
				} else {
					// need to check the password strength
					$scope.pwdStrength = password_strength($scope.password);
					if ($scope.pwdStrength != '高') {
						Message.setError(false);
						Message.setWarning(false);
						$('#main').hide();
						$scope.loginMessage = data.msg;
						$scope.loginWarning = true;
					} else {
						$location.path(path);
					}
				}
			} else {
				$scope.loginText = '登录';

				// try login with raw password
				if (!rawpwd) {
					Message.setError(false);
					$scope.login(true);
				}
			}
		});
	};
}

function LogoutCtrl($scope, $location, Module, Request, Timeout){
	var module = 'logout';
	Module.init(module, '退出登录');
	$scope.loaded = false;
	Timeout(function(){
		$scope.loaded = true;
		Request.get('/xsrf', function(){
			Request.post('/logout', {}, function(data){
				Timeout(function(){$location.path('/');}, 3000, module);
			});
		});
	}, 1000, module);
}

function deepUpdate(orgObj, newObj){
	for (i in newObj) {
		if (typeof(newObj[i]) == 'object') {
			deepUpdate(orgObj[i], newObj[i]);
		} else {
			if (orgObj[i] != newObj[i]) {
				orgObj[i] = newObj[i];
			}
		}
	}
}

function MainCtrl($scope, $routeParams, $location, Module, Timeout, Request, version){
	var module = 'main';
	Module.init(module, '首页');
	Module.initSection('server');
	$scope.version = version;
	$scope.info = null;
	$scope.loaded = false;

	$scope.detectVer = true;
	$scope.hasNewver = false;
	Request.get('/setting/upver', function(data){
		if (data.code == -1) {
			$scope.upverMessage = data.msg;
		} else if (data.code == 0) {
			var v = data.data;
			if (parseFloat(v.version) > parseFloat(version.version)
				|| (parseFloat(v.version) == parseFloat(version.version)
					&& parseInt(v.build) > parseInt(version.build))) {
				$scope.detectVer = false;
				$scope.hasNewver = true;
			}
		}
	});

	$scope.checkUpdate = function(){
		$location.path('/setting?s=upversion');
	}
	$scope.loadInfo = function(items){
		if (!items) items = '*';
		Request.get('/query/'+items, function(data){
			if ($scope.info == null) {
				$scope.info = data;
				$scope.info['server.cpustat']['total']['used_rate'] = '获取中...';
				for (var i=0; i<data['server.netifaces'].length; i++) {
					$scope.info['server.netifaces'][i]['rx_speed'] = '0';
					$scope.info['server.netifaces'][i]['tx_speed'] = '0';
				}
				if (!$scope.loaded) $scope.loaded = true;
			} else {
				if ($scope.info) {
					// caculate the cpu usage
					var stat = data['server.cpustat']['total'];
					var orgstat = $scope.info['server.cpustat']['total'];
					var used = (stat['used']-orgstat['used'])/(stat['all']-orgstat['all']);
					used = Math.round(used*10000)*10;
					var idle = 100000-used;
					used = ((used+1)/1000).toString();
					idle = ((idle+1)/1000).toString();
					stat['used_rate'] = used.substring(0,used.length-1)+'%';
					stat['idle_rate'] = idle.substring(0,idle.length-1)+'%';
					// caculate the network speeds
					var ifs = data['server.netifaces'];
					var orgifs = $scope.info['server.netifaces'];
					for (var i=0; i<ifs.length; i++) {
						var td = ifs[i]['timestamp']-orgifs[i]['timestamp'];
						if (td > 0) {
							ifs[i]['rx_speed'] = Math.round((ifs[i]['rx_bytes']-orgifs[i]['rx_bytes'])/td);
							ifs[i]['tx_speed'] = Math.round((ifs[i]['tx_bytes']-orgifs[i]['tx_bytes'])/td);
						}
					}
				}
				deepUpdate($scope.info, data);
			}
			Timeout($scope.loadInfo, 1000, module);
		});
	};
}

function FtpCtrl($scope, Module){
	var module = 'ftp';
	Module.init(module, 'FTP管理');
	$scope.loaded = true;
}

function TaskCtrl($scope, Module){
	var module = 'task';
	Module.init(module, '计划任务');
	$scope.loaded = true;
}

function SettingCtrl($scope, $routeParams, Module, Timeout, Message, Request, version){
	var module = 'setting';
	Module.init(module, '系统设置');
	Module.initSection('authinfo');
	$scope.version = version;
	$scope.showUpdateBtn = false;
	$scope.showRestartBtn = true;
	$scope.loaded = true;
	$scope.password = $scope.passwordc = '';
	
	$scope.loadAuthInfo = function(){
		Request.get('/setting/auth', function(data){
			$scope.username = data.username;
			$scope.passwordcheck = data.passwordcheck;
		});
	}
	$scope.loadServerInfo = function(){
		Request.get('/setting/server', function(data){
			$scope.ip = data.ip;
			$scope.port = data.port;
		});
	}
	$scope.updateAuthInfo = function(){
		Request.post('/setting/auth', {
			username: $scope.username,
			password: $scope.password ? hex_md5($scope.password) : '',
			passwordc: $scope.passwordc ? hex_md5($scope.passwordc) : '',
			passwordcheck: $scope.passwordcheck
		}, function(data){
			if (data.code == 0) $scope.loadAuthInfo();
		});
	};
	$scope.updateServerInfo = function(){
		Request.post('/setting/server', {
			port: $scope.port,
			ip: $scope.ip
		}, function(){
			if (data.code == 0) $scope.loadServerInfo();
		});
	};
	$scope.checkUpVersion = function(){
		$scope.upverMessage = '正在检测新版本...';
		Request.get('/setting/upver?force=1', function(data){
			if (data.code == -1) {
				$scope.upverMessage = data.msg;
			} else if (data.code == 0) {
				var v = data.data;
				if (parseFloat(v.version) > parseFloat(version.version)
					|| (parseFloat(v.version) == parseFloat(version.version)
						&& parseInt(v.build) > parseInt(version.build))) {
					$scope.upverMessage = '<table class="table table-condensed">'
						+ '<thead><tr><th colspan="2">有可用的新版本</th></tr></thead>'
						+ '<tbody><tr><td>版本信息：</td><td>v'+v.version+' b'+v.build+'</td></tr>'
						+ '<tr><td>发布时间：</td><td>'+v.releasetime+'</td></tr>'
						+ '<tr><td>变更记录：</td><td><a href="'+v.changelog+'" target="_blank">'
						+ '查看版本变更记录</a></td></tr></tbody></table>';
					$scope.updateBtnText = '开始在线升级';
					$scope.showUpdateBtn = true;
				} else {
					$scope.upverMessage = '当前已是最新版本！';
				}
			}
		});
	};
	$scope.update = function(){
		$scope.upverMessage = '正在升级，请稍候...'
		$scope.showUpdateBtn = false;
		Request.post('/backend/update', {}, function(data){
			var getUpdateStatus = function() {
				Request.get('backend/update', function(data){
					Message.setInfo('')
					if (data.msg) $scope.upverMessage = data.msg;
					if (data.status == 'finish' && data.code == 0) {
						// restart service
						$scope.upverMessage = '正在重启 VPSMate...';
						Timeout(function(){
							Request.post('/backend/service_restart', {
								service: 'vpsmate'
							}, function(data){
								var getRestartStatus = function(){
									Request.get('backend/service_restart_vpsmate', function(data){
										Message.setInfo('')
										if (data.msg) $scope.upverMessage = data.msg;
										Timeout(getRestartStatus, 500, module);
									}, function(data, status) {	// error occur because server is terminate
										if (status == 403 || status == 0) {
											$scope.upverMessage = '升级成功！请刷新页面重新登录。';
											return false;
										}
										return true;
									});
								};
								Timeout(getRestartStatus, 500, module);
							});
						}, 1000, module);
					} else {
						Timeout(getUpdateStatus, 500, module);
					}
				});
			};
			Timeout(getUpdateStatus, 500, module);
		});
	};
	$scope.restartMessage = '是否要重启 VPSMate？';
	$scope.restart = function(){
		$scope.restartMessage = '正在重启，请稍候...'
		$scope.showRestartBtn = false;
		Timeout(function(){
			Request.post('/backend/service_restart', {
				service: 'vpsmate'
			}, function(data){
				var getRestartStatus = function(){
					Request.get('backend/service_restart_vpsmate', function(data){
						if (data.msg) $scope.restartMessage = data.msg;
						Timeout(getRestartStatus, 500, module);
					}, function(data, status) {	// error occur because server is terminate
						if (status == 403 || status == 0) {
							$scope.restartMessage = '重启成功！请刷新页面重新登录。';
							return false;
						}
						return true;
					});
				};
				Timeout(getRestartStatus, 500, module);
			});
		}, 1000, module);
	};
}