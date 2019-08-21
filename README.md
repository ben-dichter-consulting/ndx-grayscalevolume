# ndx-grayscalevolume Extension for NWB:N

[![PyPI version]()

[Python Installation](#python-installation)

[Python Usage](#python-usage)

### Python Installation
```bash
pip install git+https://github.com/ben-dichter-consulting/ndx-grayscalevolume.git
```

### Python Usage

```python
from ndx_grayscalevolume import GrayscaleVolume
from datetime import datetime
from pynwb import NWBFile
import numpy as np

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

volumetric_image = GrayscaleVolume(name='My 3D image', data=np.zeros((3,4,5)))
```
