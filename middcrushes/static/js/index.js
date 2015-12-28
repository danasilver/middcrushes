(function () {
  'use strict';

  var createPattern = function () {
    var pattern = Trianglify({
      height: $(window).height(),
      width: $(window).width(),
      x_colors: 'Reds'
    });

    pattern.canvas(document.getElementById('background'));
  };

  $(window).on('resize', createPattern);

  createPattern();

})();
