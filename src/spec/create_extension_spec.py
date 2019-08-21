from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec


def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing volumetric (3D) image',
                                     name='ndx-grayscalevolume',
                                     version='0.0.1',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    GrayscaleVolume = NWBGroupSpec(
        doc='type for storing volumetric (3D) image',
        neurodata_type_def='GrayscaleVolume',
        neurodata_type_inc='NWBDataInterface',)

    GrayscaleVolume.add_dataset(name='data',
                                doc='data of image',
                                dims=('x','y','z'),
                                shape=(None,None,None),
                                dtype='float')

    new_data_types = [GrayscaleVolume]

    ns_builder.include_type('NWBDataInterface', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
