from ndx_grayscalevolume import GrayscaleVolume
from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
import numpy as np

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

grayscale_volume = GrayscaleVolume(name='test_grayscalevolume',
                                   data=np.zeros((3,4,5)))

with NWBHDF5IO('test_grayscalevolume.nwb', 'w') as io:
    io.write(nwb)

with NWBHDF5IO('test_grayscalevolume.nwb', 'r', load_namespaces=True) as io:
    io.read()
