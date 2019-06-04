function getKey() {
    let app = $("#app").val();
    let version = $("#version").val();
    $.ajax({
        url: "/getKey",
        type: "POST",
        data: {app: app, version: version},
        dataType: "text",
        success: function (result) {
            let res = JSON.parse(result);
            let html = "<div style='width:100%;height:100%;padding:5%;'>" +
                "<p><b>产品：</b>" + app + "</p><hr />" +
                "<p><b>版本：</b>" + version + "</p><hr />" +
                "<p><b>key：</b>" +
                "<pre style='background: black;color:#66FF66;padding:5%;'>" + res.key + "</pre></p><hr />" +
                "</div>"
            if (res.code == 200) {
                let area_width = "30%";
                if (device.isMobile) {
                    area_width = "80%";
                }
                //自定页
                layer.open({
                    // 在默认状态下，layer是宽高都自适应的，但当你只想定义宽度时，你可以area: '500px'，高度仍然是自适应的。
                    // 当你宽高都要定义时，你可以area: ['500px', '300px']
                    area: [area_width],
                    type: 1,
                    icon: 1,
                    skin: 'layui-layer-lan', //样式类名,目前layer内置的skin有：layui-layer-lan、layui-layer-molv
                    closeBtn: 1, //关闭按钮
                    anim: 2,
                    shadeClose: true, //开启遮罩关闭
                    title: false,
                    content: html
                });
            } else {
                //提示层
                layer.msg(res.msg, {icon: 5});
            }
        }
    })
}

