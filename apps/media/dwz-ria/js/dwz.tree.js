/**
 * @author Roger Wu
 * @version 1.0
 * added extend property oncheck
 */
 (function($){
 	$.extend($.fn, {
		jTree:function(options) {
			var op = $.extend({checkFn:null, selected:"selected", exp:"expandable", coll:"collapsable", firstExp:"first_expandable", firstColl:"first_collapsable", lastExp:"last_expandable", lastColl:"last_collapsable", folderExp:"folder_expandable", folderColl:"folder_collapsable", endExp:"end_expandable", endColl:"end_collapsable",file:"file",ck:"checked", unck:"unchecked"}, options);
			return this.each(function(){
				var $this = $(this);
				var cnum = $this.children().length;
				$(">li", $this).each(function(){
					var $li = $(this);
					
					var first = $li.prev()[0]?false:true;
					var last = $li.next()[0]?false:true; 
					$li.genTree({
						icon:$this.hasClass("treeFolder"),
						ckbox:$this.hasClass("treeCheck"),
						async:$this.hasClass("treeAsync"),
						async_url:$this.attr("async_url"),
						onaclick:$this.attr("onaclick"),
						oncheck:$this.attr("oncheck"),
						options: op,
						level: 0,
						exp:(cnum>1?(first?op.firstExp:(last?op.lastExp:op.exp)):op.endExp),
						coll:(cnum>1?(first?op.firstColl:(last?op.lastColl:op.coll)):op.endColl),
						showSub:(!$this.hasClass("collapse") && ($this.hasClass("expand") || ($this.hasClass("treeAsync")?false:(cnum>1?(first?true:false):true)))),
						isLast:(cnum>1?(last?true:false):true)
					});
				});
				$this.bindClick(op,$this.hasClass("treeCheck"),$this.attr("oncheck"),$this.attr("onaclick"));
			});
		},
		subTree:function(op, level) {
			return this.each(function(){
				$(">li", this).each(function(){
					var $this = $(this);
					setTimeout(function(){
						var isLast = ($this.next()[0]?false:true);
						$this.genTree({
							icon:op.icon,
							ckbox:op.ckbox,
							async:op.async,
							async_url:op.async_url,
							onaclick:op.onaclick,
							oncheck:op.oncheck,
							exp:isLast?op.options.lastExp:op.options.exp,
							coll:isLast?op.options.lastColl:op.options.coll,
							options:op.options,
							level:level,
							space:isLast?null:op.space,
							showSub:op.showSub,
							isLast:isLast
						});
					},1);
				});
				$(this).bindClick(op,op.ckbox,op.oncheck,op.onaclick);
			});
		},
		bindClick:function(op,ckbox,oncheck,onaclick) {
			return this.each(function(){
				var $this = $(this);
				setTimeout(function(){
					if (ckbox){
						var checkFn = eval(oncheck);
						if(checkFn && $.isFunction(checkFn)) {
							$("div.ckbox", $this).each(function(){
								var ckbox = $(this);
								ckbox.click(function(){
									var checked = $(ckbox).hasClass("checked");
									var items = [];
									if(checked){
										var tnode = $(ckbox).parent().parent();
										var boxes = $("input", tnode);
										if(boxes.size() > 1) {
											$(boxes).each(function(){
												items[items.length] = {name:$(this).attr("name"), value:$(this).val(), text:$(this).attr("text")};
											});
										} else {
											items = {name:boxes.attr("name"), value:boxes.val(), text:boxes.attr("text")};
										}		
									}								
									checkFn({checked:checked, items:items});														
								});
							});
						}
					}
					var aclickFn = eval(onaclick);
					$("a", $this).click(function(event){
						$("div." + op.selected, $this).removeClass(op.selected);
						var parent = $(this).parent().addClass(op.selected);
						$(".ckbox",parent).trigger("click");
						event.stopPropagation();
						$(document).trigger("click");
						ret = {tvalue:$(this).attr("tvalue"), text:$(this).attr("text")}
						if (aclickFn) {
							aclickFn(ret)
						}
						if (!$(this).attr("target")) return false;
					});
				},1);
			});
		},
		genTree:function(options) {
			var op = $.extend({icon:options.icon,ckbox:options.ckbox,async:options.async,async_url:options.async_url,oncheck:options.oncheck,exp:"", coll:"", showSub:false, level:0, options:null, isLast:false}, options);
			return this.each(function(){
				var node = $(this);
				var tree = $(">ul", node);
				var parent = node.parent().prev();
				var checked = 'unchecked';
				if(op.ckbox) {
					if($(">.checked",parent).size() > 0) checked = 'checked';
				}
				if (tree.size()>0) {
					node.children(":first").wrap("<div></div>");
					$(">div", node).prepend("<div class='" + (op.showSub ? op.coll : op.exp) + "'></div>"+(op.ckbox ?"<div class='ckbox " + checked + "'></div>":"")+(op.icon?"<div class='"+ (op.showSub ? op.options.folderColl : op.options.folderExp) +"'></div>":""));
					op.showSub ? tree.show() : tree.hide();
					$(">div>div:first", node).click(function(){
						var tvalue = $(">div>a", node).attr("tvalue");
						var $fnode = $(">li:first",tree);
						if (op.async && op.async_url.length > 0 && !$fnode.html()) {
							$.ajax({
								type: 'POST',
								url: op.async_url+'&tvalue='+tvalue,
								dataType: 'html',
								cache: false,
								data: function(){
									return {name: 'selectedIds', value: 'val'};
								}(),
								success: function(response){
									tree.html(response);
									tree.subTree(op, op.level + 1);
								},
								error: DWZ.ajaxError
							});
						}
						
						if ($fnode.html()) {
							if ($fnode.children(":first").isTag('a')) {
								tree.subTree(op, op.level + 1);
							}
						}
						var $this = $(this);
						var isA = $this.isTag('a');
						var $this = isA?$(">div>div", node).eq(op.level):$this;
						if (!isA || tree.is(":hidden")) {
							$this.toggleClass(op.exp).toggleClass(op.coll);
							if (op.icon) {
								$(">div>div:last", node).toggleClass(op.options.folderExp).toggleClass(op.options.folderColl);
							}
						}
						(tree.is(":hidden"))?tree.slideDown("fast"):(isA?"":tree.slideUp("fast"));
						return false;
					});
					addSpace(op.level, node);
					if(op.showSub) tree.subTree(op, op.level + 1);
				} else {
					node.children().wrap("<div></div>");			
					$(">div", node).prepend("<div class='node'></div>"+(op.ckbox?"<div class='ckbox "+checked+"'></div>":"")+(op.icon?"<div class='file'></div>":""));
					addSpace(op.level, node);
					if(op.isLast)$(node).addClass("last");
				}
				if (op.ckbox) node._check(op);
				$(">div",node).mouseover(function(){
					$(this).addClass("hover");
				}).mouseout(function(){
					$(this).removeClass("hover");
				});
				if($.browser.msie)
					$(">div",node).click(function(){
						$("a", this).trigger("click");
						return false;
					});
			});
			function addSpace(level,node) {
				if (level > 0) {					
					var parent = node.parent().parent();
					var space = !parent.next()[0]?"indent":"line";
					var plist = "<div class='" + space + "'></div>";
					if (level > 1) {
						var next = $(">div>div", parent).filter(":first");
						var prev = "";
						while(level > 1){
							prev = prev + "<div class='" + next.attr("class") + "'></div>";
							next = next.next();
							level--;
						}
						plist = prev + plist;
					}
					$(">div", node).prepend(plist);
				}
			}
		},
		_check:function(op) {
			var node = $(this);
			var ckbox = $(">div>.ckbox", node);
			var $input = node.find("a");
			var tname = $input.attr("tname"), tvalue = $input.attr("tvalue");
			var attrs = "text='"+$input.text()+"' ";
			if (tname) attrs += "name='"+tname+"' ";
			if (tvalue) attrs += "value='"+tvalue+"' ";
			
			ckbox.append("<input type='checkbox' style='display:none;' " + attrs + "/>").click(function(){
				var cked = ckbox.hasClass("checked");
				var aClass = cked?"unchecked":"checked";
				var rClass = cked?"checked":"unchecked";
				ckbox.removeClass(rClass).removeClass(!cked?"indeterminate":"").addClass(aClass);
				$("input", ckbox).attr("checked", !cked);
				$(">ul", node).find("li").each(function(){
					var box = $("div.ckbox", this);
					box.removeClass(rClass).removeClass(!cked?"indeterminate":"").addClass(aClass)
					   .find("input").attr("checked", !cked);
				});
				$(node)._checkParent();
				return false;
			});
			var cAttr = $input.attr("checked");
			if(cAttr) cAttr = eval(cAttr);
			if (cAttr) {
				ckbox.find("input").attr("checked", true);
				ckbox.removeClass("unchecked").addClass("checked");
				$(node)._checkParent();
			}
		},
		_checkParent:function(){
			if($(this).parent().hasClass("tree")) return;
			var parent = $(this).parent().parent();
			var stree = $(">ul", parent);
			var ckbox = stree.find(">li>a").size()+stree.find("div.ckbox").size();
			var ckboxed = stree.find("div.checked").size();
			var aClass = (ckboxed==ckbox?"checked":(ckboxed!=0?"indeterminate":"unchecked"));
			var rClass = (ckboxed==ckbox?"indeterminate":(ckboxed!=0?"checked":"indeterminate"));
			$(">div>.ckbox", parent).removeClass("unchecked").removeClass("checked").removeClass(rClass).addClass(aClass);
			parent._checkParent();
		}
	});
})(jQuery);