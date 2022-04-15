# vivid-firefly-importer

This project is used to import the reports from the [Vivid Money](https://vivid.money) into [Firefly III](https://github.com/firefly-iii/firefly-iii).

Vivid money provides the reports as a PDF, which is why you have to convert them to a csv.
NOTE: categories and keywords are not in the report, so they can not be mapped into firefly iii

Usage:
1. Download Vivid Bank Statement (Kontoauszug) 
2. execute Pyton script[^1]
    ```python
    python3 converter.py path/to/pdf /path/for/csv
    ```
3. open firefly importer and take csv as csv imput and vivid.json as mapping
4. done



[^1] you might have to install tika via pip3