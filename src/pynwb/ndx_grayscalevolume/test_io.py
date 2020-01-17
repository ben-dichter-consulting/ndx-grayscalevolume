from pynwb.testing import TestAcquisitionH5IOMixin, TestCase
from ndx_grayscalevolume import GrayscaleVolume
import numpy as np


class TestGrayscaleVolume(TestAcquisitionH5IOMixin, TestCase):

    def setUpContainer(self):
        return GrayscaleVolume(name='test_grayscalevolume2',
                               data=np.zeros((3, 4, 5)),
                               spatial_scale=(5., .5, 3.))
