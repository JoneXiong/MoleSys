angular.module('vpsmate.filters', []).
filter('iftrue', function(){
	return function(input, cond) {
		return cond ? input : '';
	};
}).
filter('ifmatch', function(){
	return function(input, cond) {
		return cond[0].match(new RegExp('^'+cond[1]+'$')) ? input : '';
	};
}).
filter('ifnotmatch', function(){
	return function(input, cond) {
		return cond[0].match(new RegExp('^'+cond[1]+'$')) ? '' : input;
	};
}).
filter('ifin', function(){
	return function(input, cond) {
		return typeof cond[1][cond[0]] != 'undefined' ? input : '';
	};
}).
filter('ifnotin', function(){
	return function(input, cond) {
		return typeof cond[1][cond[0]] != 'undefined' ? '' : input;
	};
}).
filter('ifverget', function(){	// version great or equal then
	return function(input, cond) {
		if (!cond[0] || !cond[1]) return '';
		var v1parts = cond[0].split('.');
		var v2parts = cond[1].split('.');
		for (var i=0; i<v1parts.length; i++) {
			if (v2parts.length == i) {
				return input;
			}
			if (v1parts[i] == v2parts[i]) {
				continue;
			}
			else if (v1parts[i] > v2parts[i]) {
				return input;
			}
			else {
				return '';
			}
		}
		if (v1parts.length != v2parts.length) {
			return '';
		}
		return input;
	};
}).
filter('netiface.updown', function(){
	return function(input) {
		return input == 'up'
			? '<span class="label label-success">启用</span>'
			: '<span class="label label-warning">停用</span>';
	};
}).
filter('netiface.encap', function(){
	return function(input) {
		if (input == 'Local Loopback') return '本地环路';
		if (input == 'Ethernet') return '以太网';
		if (input == 'Point-to-Point Protocol') return '点对点';
		if (input == 'UNSPEC') return '未识别';
		return input;
	};
}).
filter('loadavg.overload', function(){
	return function(input, cpucount) {
		if (!input) return '';
		var overload = input-cpucount;
		overload = parseInt(overload*100/cpucount);
		if (overload<0) {
			return '<span class="label label-success">'+Math.abs(overload)+'%空闲</span>';
		} else {
			if (overload>100) {
				return '<span class="label label-important">'+overload+'%过载</span>';
			} else {
				return '<span class="label label-warning">'+overload+'%过载</span>';
			}
		}
	};
}).
filter('uptime.idlerate', function(){
	return function(input) {
		if (!input) return '';
		var rate = parseInt(input);
		if (rate<10) {
			return '<span class="label label-important">'+input+'空闲</span>';
		} else if (rate<25) {
			return '<span class="label label-warning">'+input+'空闲</span>';
		} else {
			return '<span class="label label-success">'+input+'空闲</span>';
		}
	};
}).
filter('space.used', function(){
	return function(input) {
		if (!input) return '';
		var rate = parseInt(input);
		if (rate>90) {
			return '<span class="label label-important">'+input+'</span>';
		} else if (rate>75) {
			return '<span class="label label-warning">'+input+'</span>';
		} else {
			return '<span class="label label-success">'+input+'</span>';
		}
	};
}).
filter('space.free', function(){
	return function(input) {
		if (!input) return '';
		var rate = parseInt(input);
		if (rate<10) {
			return '<span class="label label-important">'+input+'</span>';
		} else if (rate<25) {
			return '<span class="label label-warning">'+input+'</span>';
		} else {
			return '<span class="label label-success">'+input+'</span>';
		}
	};
}).
filter('service.status', function(){
	return function(input) {
		if (!input) return '<span class="label">未安装</span>';
		return input == 'running'
			 ? '<span class="label label-success">运行中</span>'
			 : '<span class="label label-important">已停止</span>';
	};
}).
filter('user.lock', function(){
	return function(input) {
		return input
			? '<span class="label">锁定</span>'
			: '<span class="label label-success">正常</span>';
	};
}).
filter('site.status', function(){
	return function(input) {
		return input == 'on'
			 ? '<span class="label label-success">启用</span>'
			 : '<span class="label label-important">停用</span>';
	};
}).
filter('site.engine', function(){
	return function(input) {
		if (input == 'static')
			return '静态';
		else if (input == 'fastcgi')
			return 'FastCGI';
		else if (input == 'scgi')
			return 'SCGI';
		else if (input == 'uwsgi')
			return 'uWSGI';
		else if (input == 'redirect')
			return '跳转';
		else if (input == 'rewrite')
			return '重写';
		else if (input == 'proxy')
			return '反代';
		else
			return input;
	};
}).
filter('site.port', function(){
	return function(input) {
		if (input == '80')
			return 'http';
		else if (input == '443')
			return 'https';
		else
			return ''
	};
}).
filter('site.default_server', function(){
	return function(input) {
		return !input ? '<span class="label label-info">默认</span>' : '';
	};
}).
filter('bytes2human', function(){
	return function(n) {
		var symbols = ['G', 'M', 'K'];
		var x = symbols.length;
		var units = [];
		for (var i=0; i<x; i++) {
			units[i] = 1 << (x-i)*10;
		}
		for (var i=0; i<x; i++)
			if (n >= units[i])
				return Math.round((n/units[i])*10)/10 + symbols[i]; 
		return n+'B';
	};
});