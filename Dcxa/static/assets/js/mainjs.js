var ColorE = "#FF723D";
var ColorN = "#dadada"
var opendivid = '';
var ProgCount = 0;
function ShowLoader() {
    ProgCount = ProgCount + 1;
    $("#global-loader").show();
}
function HideLoader() {
    ProgCount = ProgCount - 1;
    if (ProgCount <= 0) {
        $("#global-loader").hide();
        ProgCount = 0;
    }
}
function ShowFileLoader(btnID) {
    var str = '<img id="loader' + btnID + '" src="images/smallLoader.gif" />';
    $("#" + btnID).parent().append(str);
    $("#" + btnID).hide();
}
function HideFileLoader(btnID) {
    $("#loader" + btnID).remove();
    $("#" + btnID).show();
}
function ShowDataLoader() {
    $("#divDataloader").show();
}
function HideDataLoader() {
    $("#divDataloader").hide();

}
function showlinkloader(id, type) {
    if (id != "") {
        if (type == 'd') {
            $('#' + id).hide();

            //  $('#' + id).parent().append('<img id="imgloading_' + id + '" src="images/small_loader.gif" />');
            $('#' + id).parent().find('#' + id).after('<img id="imgloading_' + id + '" src="images/small_loader.gif" />');

        }
        else {
            $("#imgloading_" + id).remove();
            $('#' + id).show();
        }
    }

}
function showbuttonloader(id, type) {
    if (id != "") {
        if (type == 'd') {
            $('#' + id).hide();
            $('#' + id).parent().find('*').attr('disabled', true);
            $('#' + id).after('<div class="divbtnloader" id="imgloadingbtn_' + id + '"><img src="images/small_loader.gif"> Please wait..</div>');


        }
        else {
            $("#imgloadingbtn_" + id).remove();
            $('#' + id).parent().find('*').attr('disabled', false);
            $('#' + id).show();
        }
    }
}
function setposition(id) {

    $(function () {
        $.getScript("js/jquery-ui.js", function () {

            $('#' + id).draggable({ cursor: "move", handle: '.modal-header' });
        });
    });

    //$('#' + id).css({
    //    'left': ($(window).width() / 2) - ($('#' + id).width() / 2),
    //    'top': ($(window).width() / 2) - ($('#' + id).height() / 2)
    //})


    $('#' + id).css("top", Math.max(0, (($(window).height() - $('#' + id).outerHeight()) / 2) +
        $(window).scrollTop()) + "px");

    if ($(window).width() < 481) {
        $('#' + id).css("left", "1px");
    }
    else {
        $('#' + id).css("left", Math.max(0, (($(window).width() - $('#' + id).outerWidth()) / 2) +
            $(window).scrollLeft()) + "px");
    }

}