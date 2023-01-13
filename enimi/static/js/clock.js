window.addEventListener('load', function() {
    console.log('BBBBB')
        function clockTimer()
    {
      var date = new Date();

      var time = [date.getHours(),date.getMinutes(),date.getSeconds()]; // |[0] = Hours| |[1] = Minutes| |[2] = Seconds|
      var dayOfWeek = ["Воскресенье","Понедельник","Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
      var days = date.getDay();

      if(time[0] < 10){time[0] = "0"+ time[0];}
      if(time[1] < 10){time[1] = "0"+ time[1];}
      if(time[2] < 10){time[2] = "0"+ time[2];}

      var current_time = [time[0],time[1],time[2]].join(':');
      var clock = document.getElementById("clock");
      var day = document.getElementById("dayOfWeek");

      clock.innerHTML = current_time;
      day.innerHTML = dayOfWeek[days];



      setTimeout("clockTimer()", 1000);
    }
});