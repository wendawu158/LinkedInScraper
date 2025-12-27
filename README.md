# LinkedInScraper

A LinkedIn HTML Scraper designed to look for small companies to intern at


# LinkedIn URL hacking

## The root path

### https://www.linkedin.com/search/results

This is the root path of the URL necessary to make a search.

Interestingly, linkedin doesn't seem to expect you to be able to access this specific page, and only sub paths below it.

Attached is a screenshot of what happens when you try to access this specific page

<img width="935" height="1029" alt="image" src="https://github.com/user-attachments/assets/2a158827-fddc-463f-b0f9-5dba4bf1b7fb" />


### Universal query parameters

**sid=**

This part of the URL appears to be some sort of tracking for analytics, or some sort of random string.

Either way, it seems to be completely random with no discernable pattern.

When this is removed and the truncated URL is entered, the webpage automatically adds this plus a short string of a few characters to the end of the query string.

Appears to be completely redundant for our purposes


**origin=**

Again, seems to be some sort of tracker. Completely redundant for our purposes



## Paths

### all/

Returns everything. Not very useful, as we see essentially identical content to https://www.linkedin.com/feed/


### people/

Returns profiles of people.


### content/

In the search bar, this is specified as posts. Returns posts.


### companies/

Returns a list of companies.

**companyHqGeo=%5B"location-key"%5D**

Searches for companies that have operations in those areas.

Useful location-key values include:

Continents/Regions:

* "103644278" - Asia
* "102221843" - North America
* "91000022" - NAMER (Somehow different to North America?)
* "91000007" - EMEA
* "91000003" - APAC
* "91000004" - APJ (Again, somehow different to APAC)
* "91000011" - Latin America
* "104514572" - South America
* "91000008" - MENA
* "91000001" - Middle East
* "103537801" - Africa


Countries/States:

British Isles and Ireland

* "101165590" - United Kingdom
* "104238452" - Northern Ireland
* "102299470" - England
* "100752109" - Scotland
* "104738515" - Ireland
* "105912292" - Wales


Europe

* "100565514" - Belgium
* "102890719" - Netherlands
* "101282230" - Germany
* "105015875" - France
* "106693272" - Switzerland
* "104042105" - Luxembourg


Middle East

* "100425729" - Bahrain
* "104305776" - UAE
* "100459316" - Saudi Arabia
* "103239229" - Kuwait
* "104170880" - Qatar
* "106774002" - Cyprus


Chinese Regions (in no particular order)

* "103291313" - Hong Kong
* "101316508" - Macau
* "102890883" - China
* "104187078" - Taiwan


Asia/Oceania

* "106808692" - Malaysia
* "102713980" - India
* "105490917" - New Zealand
* "101452733" - Australia
* "102454443" - Singapore
* "101355337" - Japan


Cities:

* "102257491" - London
* "100356971" - Birmingham
* "90009497" - Manchester
* "106611729" - Oxford
* "104006709" - Cambridge

* "90009487" - Glasgow

* "105178154" - Dublin

* "106032538" - Luxembourg
* "104102503" - Eindhoven

* "106383538" - Paris

* "104406358" - Geneva
* "102436504" - Zurich
  
* "103035651" - Berlin
* "106150090" - Frankfurt


  
* "105080838" - New York


### products/

Returns a list of products.


### groups/

Returns a list of groups, like discussion forums.


### services/

Returns a list of profiles of people offering services.


### events/

Returns a list of events


### learning/

Returns a list of courses


### schools/

Returns a list of schools (mostly universities)
