# SierraPy_Rega

How to use the new project?

1. Install the SierraPy project from https://github.com/hivdb/sierra-client/tree/master/python: 

in short: 
```pip install sierrapy```

2. Install pyfasta project from https://pypi.python.org/pypi/pyfasta/

in short:
```pip install pyfasta```

2. Prepare your fasta file (input.fasta) and run the following command from your command line: 

```sierrapy fasta input.fasta -q rega_query.gql -o input.json```
where 
  * input.fasta is the file you just prepared
  * rega_query.gql is the file created by Rega and available on the Github page (https://github.com/rega-cev/SierraPy_Rega/blob/master/rega_query.gql)
  * input.json is the json result given by SierraPy

3. Finally run the script parse.py (https://github.com/rega-cev/SierraPy_Rega/blob/master/parse.py) as follows:
```python parse.py -i ../path/to/input.json > ../path/to/final.csv```
where 
  * input.json is the file you got in step 2.
  * final.csv will be your final resulting output csv file
