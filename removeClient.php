<?php 

?>
<!DOCTYPE HTML>
<html>
	<head>
		<title>EB-1 v0.5.7 [End Client]</title>
		<style>
			#controls {
				border:2px solid black;
				padding:10px;
				margin:10px auto;
				width:500px;
				height:200px;
			}
			#messages {
				border:2px solid black;
				padding:10px;
				margin:10px auto;
				width:500px;
				height:300px;
				overflow-y:scroll;
			}
		</style>
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.css" />
		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
		<script>
			

			var ws = new WebSocket("ws://52.32.196.184:9001/relay");

			sendmsg = function(chan, msg) {
				var message = chan + msg;
				ws.send(message);
			};

			sendSteering = function(event, ui) {
				sendmsg("0", ui.value);
				$("#slider-value").html(ui.value);
			};

			ws.onmessage = function (message) {
				$("#messages").prepend("<br /> " + message.data);
			};

			ws.onopen = function() {
				setTimeout(function() {
					$("#slider").slider('value',13.5);
					$("#controls").show();
				}, 5000);
				
			};

			$(function () {
				$("#controls").hide();
				$("#slider").slider({
					value:100,
					min: 4,
					max: 23,
					step:0.25,
					slide: function(event, ui) {
						sendSteering(event,ui);
					},
					change: function(event, ui) {
						sendSteering(event,ui);
					}			
				});
			});
		</script>
	</head>
	<body>
		<div id="controls">
			<h3>Servo Controller</h3>
			<div id="slider"></div>
			<br /><span id="slider-value"></span>
		</div>
		<div id="messages"></div>
	</body>
</html>
