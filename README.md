# ndx-grayscalevolume Extension for NWB:N

[![PyPI version]()

[Python Installation](#python-installation)

[Python Usage](#python-usage)

### Python Installation
```bash
pip install ndx-grayscalevolume
```

### Python Usage

```python
from ndx_grayscalevolume import GrayscaleVolume
from datetime import datetime
from pynwb import NWBFile

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

spectrum = GrayscaleVolume(name, data)
```
