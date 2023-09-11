$(document).ready(function(){
    var countS = 5;
    $("#Session").html(countS);
    var countB = 2;
    $("#Break").html(countB);
    var pos = "Push Your Limit";
    var countLama;
    var posLama;
    var count;

    // Initialize the clock with 00:00
  var clock = new FlipClock($('.timer'), 0, {
    countdown: true,
    clockFace: 'MinuteCounter',
    autoStart: false,
    callbacks: {
      interval: function () {
        if (clock.getTime() == 0) {
          if (pos == "Session") {
            clock.setTime(countB * 60);
            clock.start();
            pos = "Break";
            $("#stats").html(pos);
          } else if (pos == "Break") {
            clock.setTime(countS * 60);
            clock.start();
            pos = "Session";
            $("#stats").html(pos);
          }
        }
      },
    },
  });

  // Function to update the clock display
  function updateClockDisplay() {
    var minutes = Math.floor(count / 60);
    var seconds = count % 60;
    var formattedTime = (minutes < 10 ? '0' : '') + minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
    $(".timer .middle").html(formattedTime);
  }

  // Initialize the clock display with 00:00
  updateClockDisplay();

  // Update the session length based on user input
  $("#Session").html(countS);

  // Update the break length based on user input
  $("#Break").html(countB);
    $("#stats").html(pos);
    var clock = $(".timer").FlipClock(0, {
      countdown: true,
      clockFace: 'MinuteCounter',
      autoStart: false,
      callbacks: {
        interval: function(){
          if (clock.getTime() == 0){
            if (pos == "Session"){
              clock.setTime(countB*60);
              clock.start();
              pos = "Break";
              $("#stats").html(pos);
            } else if (pos == "Break"){
              clock.setTime(countS*60);
              clock.start();
              pos = "Session";
              $("#stats").html(pos);
            }
          }        
        }
      }
    })  
    //SESSION
    $("#sessInc").on("click", function(){
      if ($("#Session").html() > 0){
        countS = parseInt($("#Session").html());
        countS+=1;
        $("#Session").html(countS);
        clock.setTime(countS*60);
      }
    });
    $("#sessDec").on("click", function(){
      if ($("#Session").html() > 1){
        countS = parseInt($("#Session").html());
        countS-=1;
        $("#Session").html(countS);
        clock.setTime(countS*60);
      }
    });
    //BREAK
    $("#breakInc").on("click", function(){
      if ($("#Break").html() > 0){
        countB = parseInt($("#Break").html());
        countB+=1;
        $("#Break").html(countB);
      }    
    });
    $("#breakDec").on("click", function(){
      if ($("#Break").html() > 1){
        countB = parseInt($("#Break").html());
        countB-=1;
        $("#Break").html(countB);
      }
    });  
    $("#start").on("click", function(){
      if (count != countS || clock.getTime()==0){
        clock.setTime(countS*60);
        pos="Session";
        $("#stats").html(pos);
      } else {
        pos = posLama;
        $("#stats").html(pos);
      }
      count = countS;    
      clock.start();    
    });
    $("#stop").on("click", function(){
      clock.stop();
      countLama = clock.getTime();
      posLama = $("#stats").html();
    });
    $("#clear").on("click", function(){
      clock.stop();
      pos = "Push Your Limit";
      $("#stats").html(pos);
      clock.setTime(0);
    });
  });