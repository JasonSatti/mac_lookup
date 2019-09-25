# Mac Lookup

mac_lookup is a Python script that is used to check the model of a MacBook based on the device's serial number..


### Installation

Install the dependencies in the requirements.txt.

```bash
pip install -r requirements.txt
```

### Usage

```python
python3 mac_lookup.py -sn "XXXX"
python3 mac_lookup.py -sn "XXXXXXXXXXXX"

```

### Usage Example

```
python3 mac_lookup.py -sn "LVDT"
2019-09-24 17:04:35,359 [INFO] maclookup: Initializing mac_lookup.
2019-09-24 17:04:35,359 [INFO] maclookup: Verifying serial number.
2019-09-24 17:04:35,359 [INFO] maclookup: Retrieving MacBook model.
MacBook Pro (15-inch, 2019)

python3 mac_lookup.py -sn "C02Z20D2LVDT"
2019-09-24 17:04:35,359 [INFO] maclookup: Initializing mac_lookup.
2019-09-24 17:04:35,359 [INFO] maclookup: Verifying serial number.
2019-09-24 17:04:35,359 [INFO] maclookup: Retrieving MacBook model.
MacBook Pro (15-inch, 2019)
```

### Testing
```python
pytest
```

### Testing Example
```
============================= test session starts ==============================
platform darwin -- Python 3.7.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0
rootdir:
collected 6 items

test_maclookup.py ......                                                 [100%]

============================== 6 passed in 0.12s ===============================
```
