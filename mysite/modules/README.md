# Making IMDb Requests and Methods

### Movie Request
| Constructor                 |  Parameters       | Description                         |
|-----------------------------|:-----------------:|:------------------------------------|
| MovieRequest()              |  title = ""       | No title is sent                    |
|                             |  year = None      | Any year is returned                |
| MovieRequest([name])        |  title = namme    | Searches for movie titled "name"    |
|                             |  year = None      | Searfhes for "name" from any year   |
| MovieRequest([name],[year]) |  title = name     | Searches for movie titled "name"    |
|                             |  year = year      | Search for "name" released in "year"|
|-----------------------------|-------------------|-------------------------------------|
