
# IMDb Requests and Methods
<br />

#### Movie Request

| Constructor                 |  Parameters       | Description                         |
|-----------------------------|:-----------------:|:------------------------------------|
| MovieRequest()              |  title = "" <br />year = None     | No title is sent<br/>Any year is selected for movie                |
| MovieRequest([Name])        |  title = [Name]<br/>year = None     | Searches for movie titled [Name]<br/>Searches for [Name] from any year   |
| MovieRequest([Name],[Year]) |  title = [Name]<br/>year = [Year]     | Searches for movie titled [Name]<br/>Search for [Name] released in [Year]   |
<br/>

##### Movie Request Methods
 + Before request
 
| Method                  | Parameters             | Description                    |
|----------------------------|:---------------------------:|------------------------------------|
| setTitle([Name])     | title = [Name]          | Sets current request to search IMDb <br/> for movie titled [Name]|
| setSearchType([type]) | movie[default],<br/> series, episode | Searches IMDb titles that are a [type]
| setYear([Year]) | year = [Year]   | Limits IMDb search to the year [Year] |
| setMovieId([ID])      | Valid IMDb Movie ID        | Search IMDb database for motion picture <br/>film with id = [ID]|
| setPlotType([type]) | short, full(default) | Returns a plot description that is either <br/>short[short] or long[full] |
<br/>
 
+ After request


 | Method                | Return                     |
 |--------------------------|------------------------------|
 | getTitle()             | Title of the result found from IMDb|
 | getYear()            | Year released of the IMDb result|
 | getPosterURL()  | URL of the poster image for the IMDb result |
 | getRated()          | Official audience rating of the released motion picture<br/>[G, PG, PG-13, etc.] |
 | getReleaseDate() | Day Month Year the motion picture was released |
 | getRuntime()      | Length of motion picture along with "min" specifier |
 | getGenre()         | Categor(y/ies) motion picture is categorized under |
 | getPlot()           | Returns plot of motion picture based on <br/>length specified by setPlotType()
 
<br/><br/>
#### Search Request <br/>

| Constructor                 |  Parameters       | Description                         |
|-----------------------------|:-----------------:|:------------------------------------|
| SearchRequest()              |  title = ""<br/>year = None      | No title is sent<br/>Any year is selected for movie                |
| SearchRequest([Name])        |  title = [Name]<br/>year = None     | Searches for movie titled [Name]<br/>Searches for [Name] from any year    |
| SearchRequest([Name],[Year]) |  title = [Name]<br/>year = [Year]     | Searches for movie titled [Name]<br/>Search for [Name] released in [Year]    |
<br/>

##### Search Request Method
+ Before request

 | Method                | Parameters            | Description                   |
 |--------------------------|:---------------------------:|:----------------------------------|
| setTitle([Name])     | title = [Name]          | Sets current request to search IMDb <br/> for movie titled [Name]|
| setSearchType([type]) | movie[default],<br/> series, episode | Searches IMDb titles that are a [type]
| setYear([Year]) | year = [Year]   | Limits IMDb search to the year [Year] |
| setPageNum([Number]) | [1-100]            | Returns a list of motion pictures from page <br/>[Number] that fulfill search requirements |
<br/>

+ After request

 | Method               | Description              |
 |--------------------------|------------------------------|
 | getTitle()             | Title of the result found from IMDb|
 | getYear()            | Year released of the IMDb result|
 | getPosterURL()  | URL of the poster image for the IMDb result |
