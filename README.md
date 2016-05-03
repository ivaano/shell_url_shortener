# shell url shortener
Little python script to be called from the shell to quickly shorten any url, using pyshorteners


I'm using this script along with keyboard maestro to quickly shorten any url that is on the clipboard

Because I'm using pyshorteners library we can use any of the services supported by pyshorteners, but I only did one that didnt require auth or api_key, and that it was short so the urls are shorted by is.gd service.

To make it work with keyboard maestro, install this script somewhere, then edit the path in the macro shell script section, also change the trigger key to whatever you want, after that just copy a url, press the trigger for the macro, and the url will be shortened and copied over to the clipboard.
