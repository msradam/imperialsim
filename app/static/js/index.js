var shape = document.getElementById("svg");


var $effect = $("#effect"),
    $circ = $(".iconCircle"),
    isFF = !!window.sidebar,
    $m1 = $(".money .one"),
    $m2 = $(".money .two"),
    $m3 = $(".money .three"),
    $eLine = $(".eLine"),
    $green = "#8DAF82",
    $blue = "#BEEAE6",
    $reg = "#414751",
    $orange = "#F47A57",
    $red = "#931429",
    $yellow = "#F9B458",
    $mReg = "#23262C";

TweenMax.set($(".dialog"), {
  visibility: "visible"
});

TweenMax.set($circ, {
  svgOrigin:"222.2, 154",
  x: 14,
  y: 58
});

//svgOrigin:"321.05, 323.3",

for (var i = 1; i < 15; i++) {
  TweenMax.set($(".d" + i), {
    opacity: 0
  });
}

//master.seek("rotateInfo+=24");

$(document).on('click', 'a.replay', function(e) {
  master.restart();
  e.preventDefault();
});

var slider = $("#slider"),
    sliderValue = {value:0};

slider.slider({
  range: false,
  min: 0,
  max: 100,
  step:.1,
  start:function() {
    master.pause();
  },
  slide: function ( event, ui ) {
    master.progress( ui.value / 100 );
  },
  stop:function() {
    master.play();
  }
});

master.eventCallback("onUpdate", function() {
  sliderValue.value = master.progress() * 100;
  slider.slider(sliderValue);
});