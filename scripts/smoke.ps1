$r = Invoke-WebRequest -Uri http://127.0.0.1:8000/health -UseBasicParsing
if ($r.StatusCode -ne 200) { throw "health failed" }
