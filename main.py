#!/usr/bin/env python
import os
#Update shopSignage

startingShopText = '''
<!DOCTYPE html>
<html>
<head>
  <title>We are Oneness</title>
  <link rel="stylesheet" type="text/css" href="./CSS/style.css">
  <link rel="stylesheet" type="text/css" media="only screen and (max-device-width: 480px)" href="./CSS/mobileStyle.css" />
</head>
<body>
<h1><a href="./index.html"> We are Oneness</h1>
<h3>Street Signage:</h3>
<div>

<center>

'''

buttons = ''''''

for file in os.listdir("./shopSignage"):
    if file.endswith(".pdf"):
        buttons = buttons + ('''
        <div class="button" id="button-a">
	    <div id="translate"></div>
	    	<a href="''' + os.path.join("./shopSignage", file) + '''">''' + file + '''</a>
	  	</div>
	  	<br>
		''')

endingShopText = '''

</center>
</div>
</body>
</html>
'''
shopSignage = open("shopSignage.html","w")
shopSignage.write(startingShopText + buttons + endingShopText)
shopSignage.close()
