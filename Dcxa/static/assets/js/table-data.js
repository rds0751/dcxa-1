$((function (e) {
    (s = $("#example").DataTable({
        dom: 'RflBrtip',
        "pageLength": 50,
        "lengthMenu": [[10, 25, 50,100,500, -1], [10, 25, 50,100,500, "All"]],
        buttons: ["copy", "excel", "pdf", "colvis"],
        responsive: !0,
        language: {
            searchPlaceholder: "Search...",
            sSearch: "",
            lengthMenu: "_MENU_ "
        }
    })), $("#example1").DataTable({
        language: {
            searchPlaceholder: "Search...",
            sSearch: "",
            lengthMenu: "_MENU_"
        }
    }), $("#example2").DataTable({
        responsive: !0,
        language: {
            searchPlaceholder: "Search...",
            sSearch: "",
            lengthMenu: "_MENU_"
        }
    });
    var a, l, r, s = $("#example-delete").DataTable({
        responsive: !0,
        language: {
            searchPlaceholder: "Search...",
            sSearch: "",
            lengthMenu: "_MENU_"
        }
    });
    $("#example-delete tbody").on("click", "tr", (function () {
        $(this).hasClass("selected") ? $(this).removeClass("selected") : (s.$("tr.selected").removeClass("selected"), $(this).addClass("selected"))
    })), $("#button").click((function () {
        s.row(".selected").remove().draw(!1)
    })), $("#example-1").DataTable((a = {
        responsive: !0,
        language: {
            searchPlaceholder: "Search...",
            sSearch: "",
            lengthMenu: "_MENU_"
        }
    }, l = "responsive", r = {
        details: {
            display: $.fn.dataTable.Responsive.display.modal({
                header: function (e) {
                    var a = e.data();
                    return "Details for " + a[0] + " " + a[1]
                }
            }),
            renderer: $.fn.dataTable.Responsive.renderer.tableAll({
                tableClass: "table border mb-0"
            })
        }
    }, l in a ? Object.defineProperty(a, l, {
        value: r,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : a[l] = r, a))
}));