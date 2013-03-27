(function ($) {
    var t = null;
    var j = null;
    var oldindex = 100;
    var thisindex = 0;

    var changeblock = function (thisindex, blockindex, slider) {
        slider.children('div:nth-child(' + blockindex + ')').addClass('ontwo');
        slider.children('div.ontop').fadeOut('slow', function () {
            slider.children('div').removeClass('ontop');
            slider.children('div').removeClass('ontwo');
            slider.children('div:nth-child(' + blockindex + ')').addClass('ontop');
            slider.children('div:nth-child(' + blockindex + ')').fadeIn('fast');
        });
        oldindex = thisindex - 1;
    }

    var runTransition = function ( thisindex, blockindex, slider) {
        slider.children('ul').children('li').removeClass('active');
        slider.children('ul').children('li:nth-child(' + thisindex + ')').addClass('active');
        slider.children('div:nth-child(' + blockindex + ')').addClass('ontwo');
        slider.children('div.ontop').fadeOut('slow', function () {
            slider.children('div').removeClass('ontop');
            slider.children('div').removeClass('ontwo');
            slider.children('div:nth-child(' + blockindex + ')').addClass('ontop');
            slider.children('div:nth-child(' + blockindex + ')').fadeIn('fast');
        });
    }

    var runTransition2 = function (thisindex, blockindex, slider) {
        slider.children('ul').children('li').removeClass('active');
        slider.children('ul').children('li:nth-child(' + thisindex + ')').addClass('active');
        j = setTimeout(function () {
            changeblock(thisindex, blockindex, slider)
        }, 300);
    }

    var setRotationwhat = function ( index, length, slider ) {
        t = setTimeout(function () {
            changeStylewhat(index, length, slider);
        }, 5000)
    }

    var changeStylewhat = function ( index, length, slider ) {
        var next = index + 1;
        if (next > length) {
            next=1;
        }
        runTransition(next, next+1, slider);
        clearTimeout(t);
        setRotationwhat(next, length, slider);
    }

    var hovon = function () {
        oldindex=100;
        clearTimeout(j);
        var self = $(this);
        var slider = self.closest('.wcc-slider');
        if (self.hasClass('active') == false) {
            thisindex = slider.children('ul').children('li').index(this);
            if (thisindex != oldindex) {
                runTransition2(thisindex + 1, thisindex + 2, slider);
                clearTimeout(t)
            }
        }
    }

    var hovoff = function () {
        var self = $(this);
        var slider = self.closest('.wcc-slider');
        setRotationwhat( thisindex + 1 , 
                slider.children('ul').children('li').length, 
                slider);
    }

    $.fn.wcc_slider = function () {
        var self = $(this);
        self.addClass('wcc-slider');
        self.children('div').first().addClass('ontop');
        self.children('div').first().fadeIn('fast');
        self.children('ul').children('li').first().addClass('active');
        self.children('ul').children('li').hoverIntent({
            sensitivity: 2,
            interval: 200,
            over: hovon,
            timeout: 200,
            out: hovoff
        });
        setRotationwhat(thisindex + 1, 
                self.children('ul').children('li').length,
                self)
    }

})(jQuery);

$(document).ready(function () {
//    $('.wcc-slider').wcc_slider(); 
});

