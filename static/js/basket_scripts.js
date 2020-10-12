window.onload = function () {
    $('.basket-item__quantity').on('change', function() {
        var optionVal = $("#basket-item__quantity").val();
        var optionText = $("#basket-item__quantity option:selected").text();
        console.log(optionVal);
        console.log(optionText);
        $.ajax ({
            url: "/basket/edit/" + optionVal + "/" + optionText + "/",
            success: function(data) {
                $('.basket-wrap').html(data.result);
            },
        });
        event.preventDefault();
    });
}

