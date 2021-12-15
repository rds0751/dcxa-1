var json;
var pagename = "/UserPages/UserKYC.aspx";
var PKID = 0;
var IsID = true;
var IsAddress = true;
var IsBank = true;
var IsProfle = true;

var SavedFileName = ""
var FID = "", FID1 = "";
var FAddress = "", FAddress1 = "";
var FBank = "";
var UploadType = "";
var UploadBtnID = "";
var UploadPath = "/imgDetail/";


function filldata() {
    ShowLoader();

    var args = {

    };
    $.ajax({
        type: "POST",
        url: pagename + "/GetData",
        data: JSON.stringify(args),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        async: true,
        cache: false,
        success: function (data) {


            if (data.d != "failure" && data.d != "Invalid Request") {
                var jsonarr = $.parseJSON(data.d);
                HideLoader();
                if (jsonarr.data.Table.length > 0) {
                    SavedFileName = jsonarr.data.Table[0].imgmember;
                    FID = jsonarr.data.Table[0].imgpan;
                    FAddress = jsonarr.data.Table[0].imgAadhar;
                    FAddress1 = jsonarr.data.Table[0].imgaadharback;
                    FBank = jsonarr.data.Table[0].imgbank;
                    if (SavedFileName != '') {
                        $("#btnProfileSelect").css("background-image", "url(/" +  SavedFileName + ")");
                    }
                    if (FID != '') {
                        $("#btnfileselect").css("background-image", "url(/" +  FID + ")");
                    }


                    if (FAddress != '') {
                        $("#btnAddressImageSelect").css("background-image", "url(/" +  FAddress + ")");
                    }
                    if (FAddress1 != '') {
                        $("#btnAddressImageSelect1").css("background-image", "url(/" +  FAddress1 + ")");
                    }
                    if (FBank != '') {
                        $("#btnfileselectBank").css("background-image", "url(/" +  FBank + ")");
                    }


                    $('#txtBankAcNo').val(jsonarr.data.Table[0].AcNo);
                    $('#txtBankName').val(jsonarr.data.Table[0].BankName);
                    $('#txtBankBranch').val(jsonarr.data.Table[0].BranchName);
                    $('#txtIFSCCode').val(jsonarr.data.Table[0].IFSC);

                    $('#txtIDNo').val(jsonarr.data.Table[0].PanNo);
                    $('#txtAddressIDNo').val(jsonarr.data.Table[0].AddrIDNo);
                    $('#dropIDType').val(jsonarr.data.Table[0].IDTypeImg);
                    $('#dropAddressType').val(jsonarr.data.Table[0].AddrTypeImg);

                    if (jsonarr.data.Table[0].ISDocReject != 1 && SavedFileName != '') {
                        IsProfle = false;
                        $('#btnsaveProfile').remove();
                        $('#PhotoStatus').html('<i class="fa fa-check-circle"></i>');
                    }



                    if (jsonarr.data.Table[0].ISDocReject != 1 && jsonarr.data.Table[0].PanNo != '' && FID != '') {
                        IsID = false;

                        $('#btnsave').remove();
                        $('#txtIDNo').prop('disabled', true);
                        $('#dropIDType').prop('disabled', true);
                        $('#IdStatus').html('<i class="fa fa-check-circle"></i>');
                    }


                    if (jsonarr.data.Table[0].ISDocReject != 1 && jsonarr.data.Table[0].AddrIDNo != '' && FAddress != '') {
                        IsAddress = false;
                        $('#btnSaveAddress').remove();
                        $('#txtAddressIDNo').prop('disabled', true);
                        $('#dropAddressType').prop('disabled', true);
                        $('#addressStatus').html('<i class="fa fa-check-circle"></i>');
                    }

                    if (jsonarr.data.Table[0].ISDocReject != 1 && jsonarr.data.Table[0].AcNo != '' && FBank != '') {
                        IsBank = false;
                        $('#btnfileselectBank').prop('disabled', true);
                        $('#txtBankAcNo').prop('disabled', true);
                        $('#txtBankName').prop('disabled', true);
                        $('#txtBankBranch').prop('disabled', true);
                        $('#txtIFSCCode').prop('disabled', true);
                        $('#btnsaveBank').remove();
                        $('#bankstatus').html('<i class="fa fa-check-circle"></i>');
                    }

                    if (jsonarr.data.Table[0].ISDocApprove == "1") {
                        IsID = false;
                        IsAddress = false;
                        IsBank = false;
                        IsProfle = true;
                        $('#IdStatus').html('<i class="fa fa-check-circle"></i>');
                        $('#addressStatus').html('<i class="fa fa-check-circle"></i>');
                        $('#bankstatus').html('<i class="fa fa-check-circle"></i>');
                        $('#PhotoStatus').html('<i class="fa fa-check-circle"></i>');

                        $('#txtBankAcNo').prop('disabled', true);
                        $('#txtBankName').prop('disabled', true);
                        $('#txtBankBranch').prop('disabled', true);
                        $('#txtIFSCCode').prop('disabled', true);

                        $('#txtAddressIDNo').prop('disabled', true);
                        $('#dropAddressType').prop('disabled', true);
                        $('#txtIDNo').prop('disabled', true);
                        $('#dropIDType').prop('disabled', true);


                        $('#btnsave').remove();
                        $('#btnsaveBank').remove();
                        $('#btnSaveAddress').remove();
                        $('#btnsaveProfile').remove();

                        $('.kycstatus').find('span').html('<i class="fa fa-check-circle"></i> &nbsp;Verified');
                        $('.kycstatus').find('span').addClass('approve');
                        $('#divRemark').hide();
                    }
                    else if (jsonarr.data.Table[0].ISDocReject == "1") {
                        $('.kycstatus').find('span').html('<i class="fa fa-warning"></i> &nbsp;' + "Rejected");
                        $('#divRemark').show();
                        $('#divRemark').html(jsonarr.data.Table[0].docremark);

                    }
                    else {
                        $('.kycstatus').find('span').html('<i class="fa fa-warning"></i> &nbsp;' + "Unverified");
                        $('#divRemark').show();
                        $('#divRemark').html(jsonarr.data.Table[0].docremark);
                    }
                }
                else {
                    $('.kycstatus').find('span').html('<i class="fa fa-close"></i> &nbsp;Not uploaded');
                }
            }
            else {
                alert("Session Timeout!");
                window.location.href = "UserLogout.aspx";
            }
        },
        error: function (x, e) {
            alert("The call to the server side failed. " + x.responseText);

            return;
        }

    });
}

function ValidateProfile() {

    var status = 1;

    if (SavedFileName == '') {
        status = 0;
        alert('Upload Profile  Image!');
        return false;
    }

    if (status == 0) {
        alert('Please fill required fields!');
        return false;
    }
    else {

        return true;

    }
}
function validateBank() {

    var status = 1;


    if ($('#txtBankAcNo').val() == '') {
        $('#txtBankAcNo').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#txtBankAcNo').css('border-color', '#dadada');
    }
    if ($('#txtBankName').val() == '') {
        $('#txtBankName').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#txtBankName').css('border-color', '#dadada');
    }
    if ($('#txtBankBranch').val() == '') {
        $('#txtBankBranch').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#txtBankBranch').css('border-color', '#dadada');
    }
    if ($('#txtIFSCCode').val() == '') {
        $('#txtIFSCCode').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#txtIFSCCode').css('border-color', '#dadada');
    }
    if (FBank == '') {
        status = 0;
        alert('Upload Bank Passbook Image!');
        return false;
    }
    if (status == 0) {
        alert('Please fill required fields!');
        return false;
    }
    else {

        return true;

    }
}


function ValidateID() {

    var status = 1;
    if ($('#dropIDType').val() == '') {
        $('#dropIDType').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#dropIDType').css('border-color', '#dadada');
    }

    if ($('#txtIDNo').val() == '') {
        $('#txtIDNo').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#txtIDNo').css('border-color', '#dadada');
    }

    if (FID == '') {
        status = 0;
        alert('Upload ID  Image!');
        return false;
    }

    if (status == 0) {
        alert('Please fill required fields!');
        return false;
    }
    else {

        return true;

    }
}


function ValidateAddress() {

    var status = 1;
    if ($('#dropAddressType').val() == '') {
        $('#dropAddressType').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#dropAddressType').css('border-color', '#dadada');
    }

    if ($('#txtAddressIDNo').val() == '') {
        $('#txtAddressIDNo').css('border-color', 'red');
        status = 0;

    }
    else {
        $('#txtAddressIDNo').css('border-color', '#dadada');
    }

    if (FAddress == '') {
        status = 0;
        alert('Upload Address Proof Front Image');
        return false;
    }
    if (FAddress1 == '') {
        status = 0;
        alert('Upload Address Proof Back Image');
        return false;
    }
    if (status == 0) {
        alert('Please fill required fields!');
        return false;
    }
    else {

        return true;

    }
}

function FunSaveProfile() {

    if (ValidateProfile()) {
        var args = {
            ImgID: SavedFileName

        };


        ShowLoader();

        $.ajax({

            type: "POST",
            url: pagename + "/UploadProfileImg",
            data: JSON.stringify(args),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            async: true,
            cache: false,
            success: function (data) {

                if (data.d != "failure" && data.d != "Invalid Login") {
                    var jsonarr = $.parseJSON(data.d);

                    HideLoader();
                    filldata();
                    if (jsonarr.length > 0 && jsonarr[0].Result == 1) {

                        alert('Saved  Successfully!');

                    }
                    else {
                        alert(jsonarr[0].Msg);
                    }


                }
                else {
                    alert(data.d);
                }

            },
            error: function (x, e) {
                alert("The call to the server side failed. " + x.responseText);
                HideLoader();
                return;
            }

        });
    }

}
function FunSaveIDProof() {

    if (ValidateID()) {
        var args = {
            ImgID: FID,
            IDNO: $("#txtIDNo").val(), IDTypeImg: $("#dropIDType").val()
        };


        ShowLoader();

        $.ajax({

            type: "POST",
            url: pagename + "/SaveIDProof",
            data: JSON.stringify(args),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            async: true,
            cache: false,
            success: function (data) {

                if (data.d != "failure" && data.d != "Invalid Login") {
                    var jsonarr = $.parseJSON(data.d);

                    HideLoader();
                    filldata();
                    if (jsonarr.length > 0 && jsonarr[0].Result == 1) {

                        alert('Saved  Successfully!');

                    }
                    else {
                        alert(jsonarr[0].Msg);
                    }


                }
                else {
                    alert(data.d);
                }

            },
            error: function (x, e) {
                alert("The call to the server side failed. " + x.responseText);
                HideLoader();
                return;
            }

        });
    }

}
function FunSaveAddressProof() {

    if (ValidateAddress()) {
        var args = {
            ImgID: FAddress, ImgID1: FAddress1,
            IDNO: $("#txtAddressIDNo").val(), IDTypeImg: $("#dropAddressType").val()
        };


        ShowLoader();

        $.ajax({

            type: "POST",
            url: pagename + "/SaveAddressProof",
            data: JSON.stringify(args),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            async: true,
            cache: false,
            success: function (data) {

                if (data.d != "failure" && data.d != "Invalid Login") {
                    var jsonarr = $.parseJSON(data.d);

                    HideLoader();
                    filldata();
                    if (jsonarr.length > 0 && jsonarr[0].Result == 1) {

                        alert('Saved  Successfully!');

                    }
                    else {
                        alert(jsonarr[0].Msg);
                    }


                }
                else {
                    alert(data.d);
                }

            },
            error: function (x, e) {
                alert("The call to the server side failed. " + x.responseText);
                HideLoader();
                return;
            }

        });
    }

}

function SaveBank() {



    if (validateBank()) {
        var args = {
            BankName: $("#txtBankName").val(), BranchName: $("#txtBankBranch").ValZero(), AcNo: $("#txtBankAcNo").val(), IFSC: $("#txtIFSCCode").val(),
            imgbank: FBank
        };


        ShowLoader();

        $.ajax({

            type: "POST",
            url: pagename + "/SaveBankDetail",
            data: JSON.stringify(args),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            async: true,
            cache: false,
            success: function (data) {

                if (data.d != "failure" && data.d != "Invalid Login") {
                    var jsonarr = $.parseJSON(data.d);

                    HideLoader();
                    if (jsonarr.length > 0 && jsonarr[0].Result == 1) {

                        alert('Saved  Successfully!');
                        filldata();
                    }
                    else {
                        alert(jsonarr[0].Msg);
                    }


                }
                else {
                    alert(data.d);
                }

            },
            error: function (x, e) {
                alert("The call to the server side failed. " + x.responseText);
                HideLoader();
                return;
            }

        });
    }

}

function FunUploadAttachment(uploadtype, btnid, uploadpath) {
    SavedFileName = "";
    OriginalFileName = "";

    UploadType = uploadtype;
    UploadBtnID = btnid;
    UploadPath = uploadpath;
    var status = 1;
    var FileType = ".PNG,.JPG,.JPEG,.BMP";

    if (status == 1) {
        var iframe = document.getElementById("ifuploadfile");
        var args = [];
        args[0] = UploadType;
        args[1] = FileType;
        args[2] = "";
        args[3] = UploadBtnID;
        iframe.contentWindow.selectAttachment(args);
    }
}
function AttachClientFileCall(Result, Msg, trID, id, filesize, filename, filext) {

    if (Result == 1) {
        HideFileLoader(UploadBtnID);
        if (UploadType == 'Profile') {
            SavedFileName = UploadPath+id;
            $("#divProfileImage").css("background-image", "url(/" + id + ")");
        }
        else if (UploadType == 'ID') {
            FID = UploadPath +id;
            $("#btnfileselect").css("background-image", "url(/" +  id + ")");
        }
        else if (UploadType == 'ID1') {
            FID1 = UploadPath +id;
            $("#btnfileselect1").css("background-image", "url(/" +  id + ")");
        }
        else if (UploadType == 'Address') {
            FAddress = UploadPath +id;
            $("#btnAddressImageSelect").css("background-image", "url(/" +  id + ")");
        }
        else if (UploadType == 'Address1') {
            FAddress1 = UploadPath +id;
            $("#btnAddressImageSelect1").css("background-image", "url(/" +  id + ")");
        }
        else if (UploadType == 'BankIDProof') {
            FBank = UploadPath +id;
            $("#btnfileselectBank").css("background-image", "url(/" +  id + ")");
        }
        else {
            SavedFileName = UploadPath +id;
            $("#btnfileselect").css("background-image", "url(/" +  id + ")");
        }


    }
    else {

        HideFileLoader(UploadBtnID);
        alert(Msg);
    }
}

$(document).ready(function () {
    $('.tabbox').on('click', 'h3', function (event) {
        event.stopImmediatePropagation();
        $(this).parent().find('.tabbox-inner').toggle();
    });

    filldata();
    $("#btnsaveProfile").click(function () {
        FunSaveProfile();
    });
    $("#btnsaveBank").click(function () {
        SaveBank();
    });

    $("#btnsave").click(function () {
        FunSaveIDProof();
    });
    $("#btnSaveAddress").click(function () {
        FunSaveAddressProof();
    });
    $('#btnProfileSelect').click(function () {
        if (IsProfle)
            FunUploadAttachment("Profile", "btnFileSelectInner", "/imgDetail/");
    });
    $('#btnfileselect').click(function () {
        if (IsID)
            FunUploadAttachment("ID", "btnFileSelectInner", "/imgDetail/");

    });
    $('#btnfileselect1').click(function () {
        if (IsID)
            FunUploadAttachment("ID1", "btnFileSelectInner1", "/imgDetail/");

    });
    $('#btnAddressImageSelect').click(function () {
        if (IsAddress)
            FunUploadAttachment("Address", "btnAddressImageSelectInner", "/imgDetail/");

    });
    $('#btnAddressImageSelect1').click(function () {
        if (IsAddress)
            FunUploadAttachment("Address1", "btnAddressImageSelectInner1", "/imgDetail/");

    });
    $('#btnfileselectBank').click(function () {
        if (IsBank)
            FunUploadAttachment("BankIDProof", "btnFileSelectInnerBank", "/imgDetail/");

    });


});