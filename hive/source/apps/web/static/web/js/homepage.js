SigurdHive = {};

SigurdHive.homepage = {
    overview: null,

    init: function() {
        var o = this.overview = $('#short-overview');
        o.find('.more-overviews-button').click(function() {
            $(this).hide();
            o.find('.hidden-feature').fadeIn();
        });
    }
};

$(function() {
    SigurdHive.homepage.init();
});