window.onload = function () {
    $(".btn-minus").click(function() {
        var currProduct = event.target.parentNode;
        var currHref = currProduct.querySelector('.basket-item__quantity');
        console.log(currHref);
        if (currHref) {
            $.ajax ({
                url: "/basket/editminus/" + currHref.name + "/",
                success: function(data) {
                    $('.basket-wrap').html(data.result);
                },
            });
        }
        event.preventDefault();
    });

    $(".btn-plus").click(function() {
        var currProduct = event.target.parentNode;
        var currHref = currProduct.querySelector('.basket-item__quantity');
        console.log(currHref);
        if (currHref) {
            $.ajax ({
                url: "/basket/editplus/" + currHref.name + "/",
                success: function(data) {
                    $('.basket-wrap').html(data.result);
                },
            });
        }
        event.preventDefault();
    });
}

