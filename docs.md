# Function defenition #

## Algorithm Manager ##

``algorithmManager`` - Class
> Class to handle and call test units to evaluate URL attributes Then allows to be called to fetch infomration as needed

``check_websiteOnline`` - Method
> Boolean function for checking if the server gives an `OK` response. Used to check if test can and should proceed

``run`` - Method
> Runs test algorithms for checking for phishy attributes using the given URL in class ``algorithmManager``. Adds errors and formatted report as a dictionary to ``algorithmManager`` ``self.report``

``runEvaluation`` - Method
> The method sends parsed URL info to test suites checking for specific phishy attributes and "phishyness points".
> Text format responses gets appended to dictionaries, where the suite name is used as keys for their responses

``createOutputString`` - Method
> Formats everything within ``self.report`` with frontend-orinted name conventions

``checkDB`` - Method
> Checks against the database if the URL has been whitelisted or has been scanned recently previously

``printFormat`` - Method
> Prints dictionary items from ``self.report`` to the terminal in a fomatted manner

## webApp ##

``index`` - Method
> Renders frontpage index from ``index.html`` flask template

``CheckURL`` - Method
> Runs algorithm manager as, then formats and presents phishy attributes and points ``index.html`` render

``FormatReport`` - Method
> ...

## test_accuracy ##

``uniquify(path)`` - Method
> Creates a unique file at `path` by appending the name with a numerator in case the file already exists

``test_accuracy(inFileName, outFolder)`` - Method

> Reads URLs from ``inFileName``, and checks which of the URLs are deemed as phishy and which are deemed benign. The output data gets written to the file ``outFolder``

## DNSresolver ##

``DNSresolver`` - Class
> Fetches and resolves information about IP, country, city, region

``resolve`` - Method
> Fetches DNS data and server geolocation

``fetchAge`` - Method
> Fetches information about domain creation date and its age

## HTMLparser ##

``HTMLparser`` - Class
> Resolves information about the HTML fetched to by the input URL

``parse`` - Method
> Gathers information and attributes from the HTML fetched to by the input URL

``fetchFaviconInfo(responedInfo)`` - Method
> Collects data about the HTML favicon

## StringParser ##

``stringParser`` - Class
> Parses information about the input URL, and sections up information into a ``URLinfo`` object

``UrlResolver`` - Method
> Extracts information form the URL, including protocol, subdomain, domain, top domain

``UnicodeCheker`` - Method
> Checks the URL for characters not included within an allowed unicode range

## url_sanatize ##

``siteValid(URL, redir)`` - Method
> Returns a boolean if the site of the URL is reachable
> ``Redir`` fetches redirects provided by the server to check.

``addScheme(url, fetch)`` - Method
> Ensures the ``url`` is prefixed with a protocol scheme.
> ``redir`` asks the server for a preferred protocol, and prefixes it to the URL

``rm_scheme(url)`` - Method
> Ensures the given ``url`` does not have a scheme prefixed

## URLinfo ##

``URLinfo`` - Class
> Stores and fetches all information about the URL

``getDNSinfo``- Method
> Fetches DNS information

``getURLstringInfo`` - Method
> Fetches URLstring information

``getHTMLinfo`` - Method
> Fetches HTML attribute information

``collectInfo`` - Method
> Stores the all of the URL information in the ``URLinfo`` object

``generateReport`` - Method
> Creates a python list from the stored information about the URL

## Config ##

Global configuration variables.

### DataBase Configurations ###

``DB = "URLanalyzer" - Database name
``DB_USERNAME = postgres`` - Database API login username
``DB_PASSWORD = “root”`` - Database API login password
``DB_HOST ='localhost'```- Database host server
``DB_PORT = '5432'`` - Port the database will communicate on


### Checklist Constants ###

``BAD_KEYWORDS = ["admin", "login", "free", "update", "security", "billing", "check", "notify", "google", "manager", "parcel", "collect", "signin", "facebook", "linkedin", "connect", "tor", "node", "apple"] `` - Keywords within a URL which can be seen as phishy


``BAD_SUBDOMAINS = ["softhouse", "google", "facebook", "linkedin", "instagram", "update", "information", "storage", "service", "safe", "reporting", "publish", "parcel", "postnord", "logistics", "collect", "free", "robux", "connect", "node"]`` - Subdomains often seen in phishy links


``REPLACEMENT_CHARACTERS = {"e": "3", "o": "0", "i": "1", "a": "@", "l": "1"}`` - Character displacements often used to trick users to think a URL is legitimate.


``BAD_CHARACTERS = [ "$", "#", "£", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_", "=", "!", "@" ]`` - Character often seen in the domain of phishy URLs


``BAD_TOPDOMAINS = ["ru", "cn", "ml", "su", "xyz", "icu", "top"]`` - Topdomains often used by phishy URLs


``BAD_URL_LENGTH = 25`` - URL domain character length limit. Longer domaines are often used in phishing links

### SSL/TLS ###

``BAD_CERT_VERSIONS = ["SSL1.0", "SSL2.0", "SSL3.0", "TLSv1.0", "TLSv1.1", "TLSv1.2"]`` - Deprecated certificate versions. Deprecated version are often used on phishing links


``MIN_CERT_VER = 2`` - Minimum certificate generation, depricated generations are unsafe and used by phishing exploiters


``MIN_CRT_AGE = 30`` - Minimum age of the certificate (in days) before seen as phishy


``BAD_CERT_COUNTRYCODES = ["AF", "LY", "RU"]`` - Countries seen as phishy as certifiers (in country code)

## SSL_resolver ##

``ssl_parser`` - Class
> Collects and holds information about certificates fetched from server linked to by URL

``ssl_sanetize(url)`` - Method
> Sanitizes the ``url`` to be compatible with the python SSL and Socket libraries

``fetch_ssl`` - Method
> Fetches certificate attributes sent to the socket

``updateSSL`` - Method
> Refetches certificate attributes as ``fetch_ssl``

## DBhandler ##

``DBhandler`` - Class
> Class handles requests to and from the PostGREsql

``delDB`` - Method
> Removes database from the server

``initDB`` - Method
> Creates database and fills a table with whitelisted domain names

``init_createWhitelist`` - Method
 > Fills a table with whitelisted domain names

``checkURLinWhitelist`` - Method
> Checks if the given URL in ``DBhandler`` exists within the whitelist table

``checkURLinpreviousSearches`` - Method
> Checks the database if the URL in ``DBhandler`` has been checked recently

``fetchPreviousSearchReport`` - Method
> Fetches previous report of a URL in case it has been searched for recently before

``fetchPreviousSearchPhishiness`` - Method
> Returns a boolean if the URL is phishy, in case it has been searched for recently before

``insertIntopreviousSearches(url, report, fishy)`` - Method
> Appends ``url`` and its corresponding ``report`` and ``fish``iness to the database

## DatabaseComparison CL ##

Checklists regarding the database.

``DatabaseComparisonCL`` - Class
> Evaluates and retains a report and points regarding the values stored in database

``runEvaluation`` - Method
> Runs test regarding the database

## DNSdataCL ##

Checklists regarding the database.

``DNSdataCL`` - Class
> Checklist object for testing and retaining a report in regards of DNS server information

``runEvaluation`` - Method 
> Runs tests regarding DNS phisnyness

``evaluateDomainCreation`` - Method
> Evaluates the domain creation date, and how phishy it can be considered

## HTMLdataCL ##

Runs test regarding the HTML fetched using the URL.

``runEvaluation`` - Method
> Run tests on the HTML in regards to phishyness

``faviconCheck`` - Method
> Checks if a favicon is present in the HTML
