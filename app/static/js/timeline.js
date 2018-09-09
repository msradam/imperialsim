var tl = new TimelineMax();

tl.from('#US', 0.5, {scaleY: 0, transformOrigin: "bottom", ease: Power2.easeOut})
  .from('#CV', 0.5, {scaleY: 0, transformOrigin: "bottom", ease: Bounce.easeOut})
.from('#IN', 0.7, {scaleX: 0, transformOrigin: "center", ease: Bounce.easeOut})