This is a custom dashboard and set of scripts for a weather display.
It's really meant specifically for my website using my XML feed, 
but I suppose it could be adapted for other sites. 
Three Scripts:

astronomy.py: Uses astral to poll for Astronomy data such as moon phase.

Current_conditions_push.py: Pulls the XML from my web server and parses it
into variables that are then pushed via the API to the dashboard.

forecast.py: Pulls JSON from WXUnderground to display forecast data. I only have
the free plan, so I only run this script every 4 hours or so via cron to 
minimize API calls.


Check out http://shopify.github.com/dashing for more information.
