
function gridUtil(p,bg_params,hide_list)	{
	this.p = p;	//html 载体
	this.cur_param = ""; // 当前gird的查询条件
	this.m_params = []; //用于保存初始查询条件(如url传过来的参数)
	this.hide_index = hide_list; //隐藏字段
	this.m_gird = $("#id_main_div",this.p).find("table");	//grid DOM本体
	this.bg_params = bg_params; //导出基本url
	
	/*
	 * 绑定点击事件
	 * ......
	 */
	/*
	 * 实时获取当前grid Dom本体
	 */
	function get_grid()
	{
		return $("#id_main_div",this.p).find("table");
	}
	this.get_grid = get_grid;
}

/****************** 公共调用部分 **********************/
/*
 * 获取当前grid util
 */
function	get_cur_util(){
	return m_util
}

/*
 * 导出
 */
function do_export(com,grid)
{
	var m_util = get_cur_util();
	var m_format = "xls";
	if (com=="导出pdf"){
		m_format = "pdf";
	}else if (com=="导出csv"){
		m_format = "csv";
	}
	var url = m_util.bg_params+"format="+m_format+"&hide="+m_util.hide_index.join(',')+"&"+m_util.cur_param;
	//window.open(url)
	$("#export_ifm").attr("src",url);
}


/*
 * grid数据加载前调用
 */
function do_Submit(){
	var p =this;
	var m_param = ''
	for (var i=0;i<p.params.length;i++)
	{
		m_param +='&'+p.params[i].name+'='+p.params[i].value;
	}
	get_cur_util().cur_param = 'page='+p.newp+'&rp='+p.rp+'&sortname='+p.sortname+'&sortorder='+p.sortorder+'&query='+p.query+'&qtype='+p.qtype+m_param
	return true;
}
/*
 *  列显隐开关回调函数
 */
function do_ToggleCol(cid, visible)
{
	var hide_index = get_cur_util().hide_index;
	if (visible)
	{
		var _tmp = [];
		for (var i=0;i<hide_index.length;i++)
		{
			if (hide_index[i]!=cid){_tmp.push(hide_index[i]);}
		}
		get_cur_util().hide_index = _tmp
	}
	else
	{
		get_cur_util().hide_index.push(cid);
	}
}