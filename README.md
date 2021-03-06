# Mac Lookup

Mac Lookup is a Python module that retrieves the model of a MacBook via lookup from Apple servers based on the device's serial number.  

### Setup

Set up a new virtual enviroment and install the requirements to run this script.

#### Install virtualenv
```via 
pip install virtualenv [--user]
```
#### Create a new virtualenv
```
virtualenv maclookup_venv
virtualenv -p /usr/local/bin/pypy maclookup_venv # using the pypy distribution
```
#### Initialize the virtualenv
```
source maclookup_venv/bin/activate
```
#### Install the requirements
```
pip install -r requirements.txt
```

### Usage

```python
python3 mac_lookup.py -s "XXXX"
python3 mac_lookup.py -s "XXXXXXXXXXXX"
```

#### Exit the virtualenv
```
deactive # which is usable only after you activate the env
```

### Usage Example

```
python3 mac_lookup.py -s "XXXX"
2019-09-24 17:04:35,359 [INFO] maclookup: Initializing mac_lookup.
2019-09-24 17:04:35,359 [INFO] maclookup: Verifying serial number.
2019-09-24 17:04:35,359 [INFO] maclookup: Retrieving MacBook model.
MacBook Pro (15-inch, 2019)

python3 mac_lookup.py -s "XXXXXXXXXXXX"
2019-09-24 17:11:32,030 [INFO] maclookup: Initializing mac_lookup.
2019-09-24 17:11:32,031 [INFO] maclookup: Verifying serial number.
2019-09-24 17:11:32,031 [INFO] maclookup: Retrieving MacBook model.
MacBook Pro (13-inch, 2018, Four Thunderbolt 3 Ports)
```

### Help

```
usage: mac_lookup.py [-h] -s SERIAL

Get MacBook model via serial number lookup.

optional arguments:
  -h, --help            show this help message and exit
  -s SERIAL, --serial SERIAL
                        Serial Number of MacBook for model lookup.
```

### Testing

```python
pytest
```
