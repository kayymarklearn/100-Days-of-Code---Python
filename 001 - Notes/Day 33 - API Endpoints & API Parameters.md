2026-01-25 19:03

Status: Incomplete

Tags: [[Day 33 - API Endpoints & API Parameters (code)]]


# **What are APIs?**
> Application Programming Interface (API)  is a set of commands, functions, protocols and objects that programmers can use to create software or interact with external systems. 
> ![[Api.png]]
   It's an interface between your program and an external system for data. If all protocols (or rules) are followed.
![[Api 2.png]]

### API Endpoints
> Usually a URL that's the location/address for find data.
> To access an API you need to make an API Request to the endpoint.
> #Example `http://api.open-notify.org/iss-now.json`
> Data returned from end points is mostly in JSON.
> In python API data can be accessed and manipulated using the 'Requests' #Module 


### Response Codes
> These tell us if our requests succeeded or not.
> Each class of response codes have their own use cases.
> 1xx: Hold on
> 2xx: Everything is succesful
> 3xx: No permission or authorization
> 4xx: Client has a problem
> 5xx: Issue with server.

### Understanding API Parameters
> This allows us to give inputs when making API requests so we can get different responses depending on our inputs. This allows us to get very specific piece of information.
## References
[Http Statuses](https://www.webfx.com/web-development/glossary/http-status-codes/)
[Requests documentation](https://requests.readthedocs.io/en/latest/)

