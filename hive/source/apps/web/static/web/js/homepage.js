SigurdHive = {};

SigurdHive.homepage = {
    overview: null,

    init: function() {
        var o = this.overview = $('#short-overview'),
            m = o.find('.more-overviews-button'),
            l = o.find('.less-overviews-button');

        m.click(function() {
            $(this).hide();
            l.fadeIn();
            o.find('.hidden-feature').fadeIn();
        });

        l.click(function() {
            $(this).hide();
            m.fadeIn();
            o.find('.hidden-feature').hide();
        });
    }
};

$(function() {
    SigurdHive.homepage.init();
});