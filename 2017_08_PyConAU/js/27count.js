Reveal.addEventListener( '27count', function() {
$(".27count")
  .countdown("2020/03/13 02:00:00", function(event) {
    weeks = event.strftime('%-w')
    y = parseInt(weeks / 52)
    m = parseInt((weeks - (y * 52)) / 4)
    timer =  "" + y + " years, " + m + " months, " + event.strftime("%-n days, ")
    timer2= event.strftime('%-H hour%!H, %-M minute%!M, %-S second%!S');
    elem = document.getElementById(event.target.className);
    elem.innerHTML = timer + "<br>" + timer2
  });
}, false );
