# Recent Birds

This was a little project to map recent bird sightings from
[eBird](https://ebird.org). The local field-naturalist's club used
to have a widget on their site that showed recent eBird data for
the area. At one point it was removed, possibly due to concerns
over reporting the locations of sensitive species like owls. I
decided to make my own version and add a map to make it easier to
see what was around. There were maps on eBird itself, but they
seemed slower and clunkier than what was possible using
[leaflet](http://leafletjs.com/) and
[openstreetmap](https://openstreetmap.org) data. The
[eBird API](https://confluence.cornell.edu/display/CLOISAPI/eBird+API+1.1) was
very straightforward and the whole thing came together in a morning.

<img src="screenshot.png" width="800">

I later added the ability to jump to a location using the
[Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation) and when that was restricted to
https contexts I switched to using the
[nominatim](https://nominatim.openstreetmap.org/) API. This worked
well for quite some time. Eventually the eBird API I was using
was deprecated in favour of one requiring an API token. Initially, I decided
to not update and just make due with the tools avaiable on eBird. For instance,
eBird has an alerts feature that will let you know if a bird you haven't seen
yet that year has been spotted in the area. This actually ends up being pretty
depressing when you receive an alert email at work and realize there's no chance
of seeing it yourself. So after a few months, I realized this map was
probably better for my mental health and decided to write a little Flask app
to run the queries and keep the API token secret.

There are at least two downsides to using this data. The first,
due to the demographics of most birdwatchers, is that reported locations are
typically those easily accessible by vehicle, not necessarily those that have
the most interesting sightings.

The second is the risk of making a mistaken identification on the basis of
expecting to see a species because others have reported seeing it in the area.
