
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


	function createMoveTable(columns,listmoves){
			var text='<table style="width:100%" class="sortable">  '





			var column_to_ignore={};
			var column_show_below={};
			var column_to_hide={};

			hide=false
			for	(i = 0; i < columns.length; i++) {
			column_to_ignore[columns[i]]=0;
			column_show_below[columns[i]]=0;
			column_to_hide[columns[i]]=0;
			
				if (hide)
				{
				column_to_hide[columns[i]]=1;
				column_to_ignore[columns[i]]=1;
				column_show_below[columns[i]]=1;
				}
			if (columns[i]==='x') // every column after that columns will appear below the video
			{	hide=true
				column_to_hide[columns[i]]=1;
				column_to_ignore[columns[i]]=1;
				column_show_below[columns[i]]=0;
			}

			}
			column_to_ignore['start']=1;
			column_to_ignore['end']=1;
			column_to_ignore['youtubeid']=1;
			column_to_ignore['name']=1;
			column_to_ignore['dance']=1;
			column_to_ignore['comments']=1;
			column_show_below['start']=0;
			column_show_below['end']=0;
			column_show_below['youtubeid']=0;
			column_show_below['name']=0;
			column_show_below['dance']=0;
			text+= '<tr><th>name</th>'

			sub_column_names=[]
			sub_column_displaynames=[]
			sub_column_names.push('name')
			sub_column_displaynames.push('name')


			for	(i = 0; i < columns.length; i++) {
					

					if (column_to_ignore[columns[i]]==0){
					text+='<th >'+columns[i]+'</th>'
					sub_column_names.push(columns[i])
					sub_column_displaynames.push(columns[i])
					}
					if (column_to_hide[columns[i]]==1){
					text+='<th hidden>'+columns[i]+'</th>'
					sub_column_names.push(columns[i])
					sub_column_displaynames.push(columns[i]);
					}
					}
			text+='</tr>'
	
		
			for	(index = 0; index < listmoves.length; index++) {
				move=listmoves[index]
				text+= '<tr>'
			    	text +=   "<td><a class='croppedVideo' videoid='"+move['youtubeid']
				text+="' start="+move['start']+" end="+move['end']+" href='#'>"+move['name']+"</a></td>"
				for	(i = 0; i < columns.length; i++) {
	
						if (column_to_ignore[columns[i]]==0){
						text+='<td>'+move[columns[i]]+'</td>'
						}
						if (column_to_hide[columns[i]])
							{text+='<td hidden>'+move[columns[i]]+'</td>'}
					

					}

			   	
				text+='</tr>'
			  }
			text+=  "</table> "
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
				comments=''
				$(this).parent().parent().children('td').each(function( index ) {
  				console.log( index +":"+ sub_column_names[index]+": " + $( this ).text() );
				if (column_show_below[sub_column_names[index]]){
				comments+='<div>'+'<span class="sub_column_name">'+sub_column_displaynames[index]+': '+'</span>'+$( this ).text()+'</div>' }
				});
				$("#video_comments").html(comments)
				
			});

			}


	$(document).ready(function() {





if ($.urlParam('source')=='google_spreadsheet')
	{
	spreadsheet_link='https://docs.google.com/spreadsheets/d/'+$.urlParam('id');

	sheetsNamesHtml=''

	if ($.urlParam('sheet'))
        {sheetNumber=parseInt($.urlParam('sheet'))}
	else
	{sheetNumber=1}

	$.ajax({
	  dataType: "json",
	  url: 'https://spreadsheets.google.com/feeds/worksheets/'+$.urlParam('id')+'/public/full?alt=json',
		success: function(json) {  
		  
			listSheetsJson=json.feed.entry  

			
			
			listSheets=[]
			for	(index = 0; index < listSheetsJson.length; index++) {
				sheetJson=listSheetsJson[index]
				sheetName=sheetJson.title['$t']
				href=$.query.set("sheet", index+1).toString()
				if (index+1==sheetNumber)
				{sheetsNamesHtml+="<a class='dancename' id='selecteddance'  href='"+href+"' > "+ sheetName+" </a>"}
				else
				{sheetsNamesHtml+="<a class='dancename'  href='"+href+"' >"+ sheetName+"</a> "}
				console.log(sheetsNamesHtml)
				console.log(sheetJson.link[0]['href'])
			}
			$("#sheets").html(sheetsNamesHtml);
			},	 

    	   error: function(e) {
       			console.log(e.message);}
	});
	
	
	

	


	$.ajax({
	  dataType: "json",
	  url: 'https://spreadsheets.google.com/feeds/list/'+$.urlParam('id')+'/'+sheetNumber+'/public/values?alt=json',
		success: function(json) {    
			listmovesJson=json.feed.entry   
			var columns=[]
			for (k in listmovesJson[0]){
			if (k.substring(0, 4)==='gsx$'){
					columns.push(k.substring(4))
					console.log(k.substring(4))}
				}
			listmoves=[]
			for	(index = 0; index < listmovesJson.length; index++) {
				moveJson=listmovesJson[index]
				move={}
				for	(i = 0; i < columns.length; i++) {
					move[columns[i]]=moveJson['gsx$'+columns[i]].$t
					}				
				listmoves.push(move);
			}
			createMoveTable(columns,listmoves);
			},
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
			var listmovesCSV=$.csv.toArrays(atob(json.content));
			var text='<table style="width:100%" class="sortable">  <tr>'
			columns=listmovesCSV[0]
			listmoves=[]

			for	(index = 1; index < listmovesCSV.length; index++) {
				
				movecsv=listmovesCSV[index]
				move={}
				for	(i = 0; i < columns.length; i++) {
				move[columns[i]]=movecsv[i]}
				listmoves.push(move)
			}
			createMoveTable(columns,listmoves);

			},
    		error: function(e) {
       			console.log(e.message);}
	});
	}



if (typeof spreadsheet_link !== typeof undefined && spreadsheet_link !== false) {

$("#playerwithplaylist").html("<div id='left'> <h3 id='title'>click on a video on the right</h3>  <div id='player'></div>  <button type='button'  class='speedButton' speed=1>normal speed</button>  <button type='button' class='speedButton' speed=0.5 >slow x2</button>  <button type='button' class='speedButton' speed=0.25 >slow x4</button>  <p id='video_comments'></p></div><div id='right'> You can create your own playlist by following the instructions  <a href='https://github.com/martinGithub/dance_moves/newplaylist.html'>here</a> You can go <a href='https://github.com/martinGithub/dance_moves'>here</a> to get a python script that downloads the edited videos.You can contribute to this list by editing the file <a class='spreadsheet_link'>here</a>  once you got the permissions from the owner of the file.<br> <br><div id='listmoves'></div></div>'");
$('a.spreadsheet_link').attr('href',spreadsheet_link)
}

		$('button.speedButton').on("click", function (e) {
			e.preventDefault();
			player.setPlaybackRate($(this).attr('speed'));});
		});

	$(window).scroll(function(){
    		$("#left").css("margin-top",Math.max(-250,0-$(this).scrollTop()));});



