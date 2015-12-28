(function () {
  'use strict';

  var createPattern = function () {
    var height = $('body').height() < $(window).height()
      ? $(window).height()
      : $('body').height();

    var pattern = Trianglify({
      height: height - 50,
      width: $(window).width(),
      x_colors: 'Reds'
    });

    pattern.canvas(document.getElementById('background'));
  };

  $(window).on('resize', createPattern);

  createPattern();

})();
