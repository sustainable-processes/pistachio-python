# Pistachio Python SDK

This is the repository for our unofficial python SDK for the Pistachio API.

## Installation

```bash
pip install git+https://github.com/sustainable-processes/pistachio-python
```


## Usage

**SSH Tunnel**

If you are not running this on a the server, you need to set up an ssh tunnel to port 8080 (while logged into the VPN.) You can map to any open port on your machine. Below, I used 8898.

 ```bash
$ ssh -NfL localhost:8898:localhost:8080 csrid@ceb-307-40-ldo.ceb.private.cam.ac.uk
```
**Sessions**

You can set up a session in one of two ways:
```python
from pistachio import Pistachio
base_url = "http://localhost:8898/" #Should match the port from above

# Method 1: with block
with Pistachio(base_url=base_url) as p:
    # Do whatever you need here
    # The session will be closed when the block is exited 
    p.search("suzuki coupling")
    
# Method 2: manually
p = Pistachio(base_url=base_url)
p.renew_session()
p.search("suzuki coupling")
p.end_session()
```

**Methods**

Parse a textual query without running a search.
```python
p.parse("GSK")
# {
# "str": "GSK",
# "grouped": True,
# "cacheAllowed": True,
# "tags": [{"end": 3, "tag": "ASSIGNEE", "val": "GlaxoSmithKline"}],
# }
```

Generate suggestions of queries for the input text.
```python
p.suggest("Suzuki")
# {'suggestions': ['suzuki coupling', 'suzuki-type coupling'],
#  'draw': 0,
#  'tags': [{'end': 6, 'tag': 'NONE'}]}
```

Search for reactions.
```python
p.search("suzuki coupling")
```

Get details about a reaction by its id.
```python
p.get_details("176")
```

Summarize the data for each type of result of a query.
```python
p.summary("suzuki_coupling")
```


