# LinkedInScraper

A LinkedIn HTML Scraper designed to look for small companies to intern at


# LinkedIn URL hacking

# The root path

## https://www.linkedin.com/search/results

This is the root path of the URL necessary to make a search.

Interestingly, linkedin doesn't seem to expect you to be able to access this specific page, and only sub paths below it.

Attached is a screenshot of what happens when you try to access this specific page

<img width="935" height="1029" alt="image" src="https://github.com/user-attachments/assets/2a158827-fddc-463f-b0f9-5dba4bf1b7fb" />


## Universal query parameters

# sid=

This part of the URL appears to be some sort of tracking for analytics, or some sort of random string.

Either way, it seems to be completely random with no discernable pattern.

When this is removed and the truncated URL is entered, the webpage automatically adds this plus a short string of a few characters to the end of the query string.

Appears to be completely redundant for our purposes


# origin=

Again, seems to be some sort of tracker. Completely redundant for our purposes



# Paths

## all/

Returns everything. Not very useful, as we see essentially identical content to https://www.linkedin.com/feed/


## people/

Returns profiles of people.


## content/

In the search bar, this is specified as posts. Returns posts.


## companies/

Returns a list of companies.

### companyHqGeo=%5B"location-keys"%5D

Searches for companies that have operations in those areas.

Useful location-key values include:

**Continents/Regions:**

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


**Countries/States:**

British Isles and Ireland:

* "101165590" - United Kingdom
* "104238452" - Northern Ireland
* "102299470" - England
* "100752109" - Scotland
* "104738515" - Ireland
* "105912292" - Wales


Europe:

* "100565514" - Belgium
* "102890719" - Netherlands
* "101282230" - Germany
* "105015875" - France
* "106693272" - Switzerland
* "104042105" - Luxembourg


Middle East:

* "100425729" - Bahrain
* "104305776" - UAE
* "100459316" - Saudi Arabia
* "103239229" - Kuwait
* "104170880" - Qatar
* "106774002" - Cyprus


Chinese Regions (in no particular order):

* "103291313" - Hong Kong
* "101316508" - Macau
* "102890883" - China
* "104187078" - Taiwan


Asia/Oceania:

* "106808692" - Malaysia
* "102713980" - India
* "105490917" - New Zealand
* "101452733" - Australia
* "102454443" - Singapore
* "101355337" - Japan


**Cities:**

UK and Ireland:

* "102257491" - London
* "100356971" - Birmingham
* "90009497" - Manchester
* "106611729" - Oxford
* "104006709" - Cambridge
* "90009487" - Glasgow
* "90009485" - Edinburgh
* "90009484" - Dundee
* "105178154" - Dublin


Low Countries:

* "106032538" - Luxembourg
* "104102503" - Eindhoven
* "90010383" - Amsterdam


Scandinavian Countries:

* "90009617" - Copenhagen
* "90010069" - Oslo
* "90010409" - Stockholm
* "103079818" - Reykjavik


France:

* "106383538" - Paris
* "90009691" - Toulouse


Switzerland:

* "104406358" - Geneva
* "102436504" - Zurich


Germany:

* "103035651" - Berlin
* "106150090" - Frankfurt
* "90009735" - Munich
* "90009750" - Stuttgart


Italy:

* "90009936" - Milan


USA:

* "90000070" - New York
* "90000049" - Los Angeles
* "90000097" - Washington DC
* "104116203" - Seattle
* "103112676" - Chicago
* "102277331" - San Francisco
* "90000042" - Houston
* "90000007" - Boston
* "90000512" - Mineeapolis / St Paul
* "90000035" - Detroit
* "90010472" - San Diego
* "119294018" - Orange County
* "90000716" - Salt Lake City
* "90000031" - Dallas / Fort Worth


Canada:

* "90009551" - Toronto


Brazil:

* "105871508" - Sao Paulo


UAE:

* "104524176" - Abu Dhabi
* "106204383" - Dubai


Australia:

* "90009521" - Melbourne


India:

* "90009626" - Delhi
* "90009639" - Mumbai
* "90009633" - Bengaluru
* "90009647" - Chennai


China:

* "102772228" - Shanghai
* "102454443" - Shenzhen
* "103291313" - Hong Kong


Japan:

* "90009987" - Tokyo


South Korea:

* "90010114" - Seoul


Singapore:

* "106750182" - Singapore


Thailand:

* "90010335" - Bangkok


### companySize=%5B"size-keys"%5D

Searches for companies with that number of employees:

Size Chart:
* "A" - Appears to be unused (Why?)
* "B" - 1 - 10 employees
* "C" - 11 - 50 employees
* "D" - 51 - 200 employees
* "E" - 201 - 500 employees
* "F" - 501 - 1000 employees
* "G" - 1001 - 5000 employees
* "H" - 5001 - 10000 employees
* "I" - 10001+ employees

Note: LinkedIn calculates company size by counting how many members list that company as their current employer on their profiles, and in practise most companies are slightly larger than their category.

## products/

Returns a list of products.


## groups/

Returns a list of groups, like discussion forums.


## services/

Returns a list of profiles of people offering services.


## events/

Returns a list of events


## learning/

Returns a list of courses


## schools/

Returns a list of schools (mostly universities)
