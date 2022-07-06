window.onload = function() {
  action();
}

function action() {
  $("#action1").click(function() {
    $.ajax({
      type: 'GET',
      url: 'api/sayHello',
      dataType: 'json',
      data: {
        name: 'John',
        location: 'Boston',
        dateTime: new Date().getTime(),
      },
      success: function(data, textStatus, jqXHR) {
        console.log("data" + data);
        console.log("textStatus" + textStatus);
        console.log("jqXHR" + jqXHR);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error("jqXHR" + jqXHR);
        console.error("textStatus" + textStatus);
        console.error("errorThrown:" + errorThrown);
      }
    });
  })
}