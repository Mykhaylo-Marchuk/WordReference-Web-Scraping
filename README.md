# Major fix

The program was unable to access the RAE website (Error 403: Forbidden) 
with the `responses` package, so, after completing the project using a 
completely different website (WordReference), I came back to this issue 
and fixed it by switching to the `urllib.request` module instead. 

The project now uses the correct website thanks to this fix.