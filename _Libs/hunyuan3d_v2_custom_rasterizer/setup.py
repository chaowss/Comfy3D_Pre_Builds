from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# build custom rasterizer
# build with `python setup.py install`
# nvcc is needed

custom_rasterizer_module = CUDAExtension('hunyuan3d_v2_custom_rasterizer_kernel', [
    'cpp_lib/custom_rasterizer_kernel/rasterizer.cpp',
    'cpp_lib/custom_rasterizer_kernel/grid_neighbor.cpp',
    'cpp_lib/custom_rasterizer_kernel/rasterizer_gpu.cu',
])

setup(
    packages=find_packages(),
    version='0.1',
    name='hunyuan3d_v2_custom_rasterizer',
    include_package_data=True,
    package_dir={'': '.'},
    ext_modules=[
        custom_rasterizer_module,
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
