



	function getSeconds(tt)
	{
	s=tt.split(":");
	sec=s[0]*3600+s[1]*60+s[2]*1;
	return sec
	}

	$.urlParam = function(name){// from http://stackoverflow.com/questions/19491336/get-url-parameter-jquery
	    var href=window.location.href
	    if (href.slice(-1)=='/')
		{href=href.slice(0,-1)
		}	
	    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(href);
	    if (results==null){
	       return null;
	    }
	    else{
	       return results[1] || 0;
	    }
	}

	
	
	videoId='Oi1BcouEmio'//black video

	var maxtime = 20; 
	var mintime = 10; 
	var idbeat=1

	// find documentation here https://developers.google.com/youtube/iframe_api_reference
      	// 2. This code loads the IFrame Player API code asynchronously.
      	var tag = document.createElement('script');

      	tag.src = "https://www.youtube.com/iframe_api";
      	var firstScriptTag = document.getElementsByTagName('script')[0];
      	firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      	// 3. This function creates an <iframe> (and YouTube player)
      	//    after the API code downloads.
      	var player;
      	function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
		  height: '390',
		  width: '640',
		  videoId: videoId,
		  playerVars : {
		    'autoplay' : 0, 'controls': 1},
		  events: {
		    'onReady': onPlayerReady,
		    'onStateChange': onPlayerStateChange
		  }});}
	var reached = false;
      	// 4. The API will call this function when the video player is ready.
      	function onPlayerReady(event) {
		player.seekTo(mintime, 0);
		player.pauseVideo();
		//player.setPlaybackRate(0.3);

	
	var interval = setInterval(function(){
		//console.log(player.getCurrentTime())
		//console.log(mintime)
		//console.log(maxtime)

		if(player.getCurrentTime() < maxtime){reached= false;}
		if((player.getCurrentTime() >= maxtime || player.getCurrentTime() < mintime) &&!reached) {
			console.log('coucou')
			//clearInterval(interval);
			reached = true;
			timeReached(event);
		    }},100);  }

     	function onPlayerStateChange(event) {
        	if (event.data == 1) {}}

	function timeReached(event){		
		event.target.seekTo(mintime, true);// you need to set true or it won't work ! 
		console.log(player.getCurrentTime())}


	function stopVideo() {
		player.stopVideo();
	      }



	$(document).ready(function() {


if ($.urlParam('source')=='google_spreadsheet')
	{
	spreadsheet_link='https://docs.google.com/spreadsheets/d/'+$.urlParam('id');

$.ajax({
	  dataType: "json",
	  url: 'https://spreadsheets.google.com/feeds/list/'+$.urlParam('id')+'/default/public/values?alt=json',
		success: function(json) {    
			listmoves=json.feed.entry   
			var text='<table style="width:100%">  <tr>'
			
			
			for	(index = 0; index < listmoves.length; index++) {
				move=listmoves[index]
				text+= '<tr>'
			    	text +=   "<td><a class='croppedVideo' videoid='"+move.gsx$youtubeid.$t
				text+="' start="+move.gsx$start.$t+" end="+move.gsx$end.$t+" href='#'>"+move.gsx$name.$t+"</a></td>"
			   	text +=    "<td>"+move.gsx$level.$t+"</td> "
				text +=    "<td>"+move.gsx$beatcount.$t+"</td> "
				text+='</tr>'
			  }
			text+=  "</tr></table> "
			$("#listmoves").html(text); 
		
			$('a.croppedVideo').on("click", function (e) {
				e.preventDefault();
				player.loadVideoById($(this).attr('videoid'));
				maxtime=getSeconds($(this).attr('end'));
				mintime=getSeconds($(this).attr('start'));
				console.log($(this).attr('videoid')+ ' '+ mintime+ ' '+mintime)
				$("#title").html($(this).text()); 
				player.seekTo(mintime, 0);
				idbeat=1
			});},
    		error: function(e) {
       			console.log(e.message);}
	});
	}

	else{
spreadsheet_link=$('#playerwithplaylist').attr('spreadsheet');


	$.ajax({
	  dataType: "json",
	  url: $('#playerwithplaylist').attr('rawspreadsheet')+'?ref=listmoves',
		success: function(json) {       
			//$("#listmoves").text('worked?'); 
			var listmoves=$.csv.toArrays(atob(json.content));
			var text='<table style="width:100%">  <tr>'
			columns=listmoves[0]
	var associativeArray = {};
for	(i = 0; i < columns.length; i++) {
associativeArray[columns[i]]=i
}
			for	(index = 1; index < listmoves.length; index++) {
				move=listmoves[index]
				text+= '<tr>'
			    	text +=   "<td><a class='croppedVideo' videoid='"+move[associativeArray['youtubeid']]
				text+="' start="+move[associativeArray['start']]+" end="+move[associativeArray['end']]+" href='#'>"+move[associativeArray['name']]+"</a>"
				text+='</tr>'
			  }
			text+=  "</tr></table> "
			$("#listmoves").html(text); 
		
			$('a.croppedVideo').on("click", function (e) {
				e.preventDefault();
				player.loadVideoById($(this).attr('videoid'));
				maxtime=getSeconds($(this).attr('end'));
				mintime=getSeconds($(this).attr('start'));
				console.log($(this).attr('videoid')+ ' '+ mintime+ ' '+mintime)
				$("#title").html($(this).text()); 
				player.seekTo(mintime, 0);
				idbeat=1
			});},
    		error: function(e) {
       			console.log(e.message);}
	});
	}



if (typeof spreadsheet_link !== typeof undefined && spreadsheet_link !== false) {

$("#playerwithplaylist").html("<div id='left'> <h3 id='title'>click on a video on the right<h3>  <div id='player'></div>  <button type='button'  class='speedButton' speed=1>normal speed</button>  <button type='button' class='speedButton' speed=0.5 >slow x2</button>  <button type='button' class='speedButton' speed=0.25 >slow x4</button> <!--<button type='button' class='BPM'  >click on 1</button>--> <p class='video_comments'></p></div><div id='right'> You can create your own playlist by following the instructions  <a href='../newplaylist.html'>here</a> You can go <a href='https://github.com/martinGithub/dance_moves'>here</a> to get a python script that download the edited videos.You can contribute to this list by editing the file <a class='spreadsheet_link'>here</a>  once you got the permissions from the owner of the file.<br> <br><div id='listmoves'></div></div>'");
$('a.spreadsheet_link').attr('href',spreadsheet_link)
}

		$('button.speedButton').on("click", function (e) {
			e.preventDefault();
			player.setPlaybackRate($(this).attr('speed'));});
		});

	$(window).scroll(function(){
    		$("#left").css("margin-top",Math.max(-250,0-$(this).scrollTop()));});



