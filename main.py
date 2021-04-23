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
<h1><a href="./index.html"> We are Oneness</a></h1>
<h3>Shop Signage:</h3>
<div>

<center>

'''

shopButtons = ''''''

for file in os.listdir("./shopSignage"):
    if file.endswith(".pdf"):
        shopButtons = shopButtons + ('''
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
shopSignage.write(startingShopText + shopButtons + endingShopText)
shopSignage.close()

#Update streetSignage

startingStreetText = '''
<!DOCTYPE html>
<html>
<head>
  <title>We are Oneness</title>
  <link rel="stylesheet" type="text/css" href="./CSS/style.css">
  <link rel="stylesheet" type="text/css" media="only screen and (max-device-width: 480px)" href="./CSS/mobileStyle.css" />
</head>
<body>
<h1><a href="./index.html"> We are Oneness</a></h1>
<h3>Street Signage:</h3>
<div>

<center>

'''

streetButtons = ''''''

for file in os.listdir("./streetSignage"):
    if file.endswith(".pdf"):
        streetButtons = streetButtons + ('''
        <div class="button" id="button-a">
	    <div id="translate"></div>
	    	<a href="''' + os.path.join("./shopSignage", file) + '''">''' + file + '''</a>
	  	</div>
	  	<br>
		''')

endingStreetText = '''

</center>
</div>
</body>
</html>
'''
streetSignage = open("streetSignage.html","w")
streetSignage.write(startingStreetText + streetButtons + endingStreetText)
streetSignage.close()
