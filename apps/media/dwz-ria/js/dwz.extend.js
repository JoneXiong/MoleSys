/**
 * @author Johan
 */
(function($){
	
	$.fn.extend({
		selectedTodialog: function(){
			
			function _getIds(selectedIds, targetType){
				var ids = "";
				var $box = targetType == "dialog" ? $.pdialog.getCurrent() : navTab.getCurrentPanel();
				$box.find("input:checked").filter("[name='"+selectedIds+"']").each(function(i){
					var val = "K="+$(this).val()+"&T="+$(this).attr("title");
					ids += i==0 ? val : "&"+val;
				});
				return ids;
			}
			return this.each(function(){
				var $this = $(this);
				var options = {mask:true, 
									width:$this.attr('width')||820, height:$this.attr('height')||400,
									maxable:eval($this.attr("maxable") || "true"),
									resizable:eval($this.attr("resizable") || "true")
								};
				var selectedIds = $this.attr("rel") || "ids";
				var postType = $this.attr("postType") || "map";

				$this.click(function(){
					var ids = _getIds(selectedIds, $this.attr("targetType"));
					if (!ids) {
						alertMsg.error($this.attr("warn") || DWZ.msg("alertSelectMsg"));
						return false;
					}
					if ($this.attr("onlyone")&& ids.split("=").length>3){
						alertMsg.error($this.attr("warn") || DWZ.msg("alertSelectOnlyOneMsg"));
						return false;
					}
					function _doPost(){
//						$.ajax({
//							type:'POST', url:$this.attr('href'), dataType:'json', cache: false,
//							data: function(){
//								if (postType == 'map'){
//									return $.map(ids.split(','), function(val, i) {
//										return {name: selectedIds, value: val};
//									})
//								} else {
//									var _data = {};
//									_data[selectedIds] = ids;
//									return _data;
//								}
//							}(),
//							success: navTabAjaxDone,
//							error: DWZ.ajaxError
//						});
						url = $this.attr('href')+"&"+ids
						$.pdialog.open(url, ids, $this.attr("title") || $this.text(), options);
					}
					_doPost();
					return false;
				});
				
			});
		}
	});
})(jQuery);

