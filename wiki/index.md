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



