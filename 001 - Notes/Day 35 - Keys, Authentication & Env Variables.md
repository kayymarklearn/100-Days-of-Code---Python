2026-01-28 01:17

Status: incomplete

Tags:


# **API Keys**
> Special code used for authenticating access to an API.
> It's kind of like a personal account number and password.

> They can be added to a request by creating a dict of all parameters to be used as part of the request.
> ```
> API_KEY = 'keygoeshere'
> URL="https://api.openweathermap.org/data/2.5/forecast"

parameters = {

	'lat': "25.972230",

	'lon': "-6.090050",

	'appid': API_KEY

	}

response = requests.get(url=URL, params=parameters)

response.raise_for_status()
> ```

### Environment variables
> Environment variables can be used to store credentials (like API keys, auth tokens etc.) to prevent access
> by unauthorized access.
> Environment variables can be accessed by using the environ method from the python os module
> ```
> import os
> API_KEY = os.environ.get("API_KEY") # Recommeded, easier to manage errors
> OR
> API_KEY = os.environ["API_KEY"]
> # Environment variables can be set in the terminal by using the export command
> export API_KEY = "yourapikeygoeshere"
> ```
## References
