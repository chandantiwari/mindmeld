
function evaluate_mbti() {
  for (var i=0;i<70;i++){
    var j = i+1;
    res = $("input[name='group"+j+"']:checked").val();
    if (res == undefined) {
	$('#mbtierror').html("Question " + j + " is not answered");
	return;
      }
  }    
  var list = "";
  for (var i=0;i<70;i++){
    var j = i+1;
    res = $("input[name=group"+j+"]:checked").val();
    list += ":" + res;
  }  
  HACK="#spiller";    
  $.getJSON('/evaluate_mbti', { 'answers': list},
     function(response){
       $('#mbtierror').html("");
       $('#mbtiresult').attr('href', '/mweb/mbti/' + response.toLowerCase() + ".html" + HACK);
       $('#mbtiresult a').attr("target", "_new");
       $('#mbtiresult a').text(response); 
       $("#mbtiresult").show()       
     }
  );
}       

