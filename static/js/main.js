function attachHandlers() {
    $("#clear").click(clear);
    $("#save").click(save);
}

function clear() {
    var config = {type: "get"}
    $.ajax("/clear", config);
}

function save() {
    var config = {type: "get"}
    var title = $("#title-field").val()
    var body = $("#body-field").val()
    $.ajax("/save?title=" + encodeURIComponent(title) + "&body=" + encodeURIComponent(body), config);
}

$(document).ready(attachHandlers);
