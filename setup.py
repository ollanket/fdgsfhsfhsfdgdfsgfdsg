import os

os.system('wget https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs1000/ghostpdl-10.0.0.tar.gz')

os.system('tar -xf ghostpdl-10.0.0.tar.gz')

os.system('cd ghostpdl-10.0.0 && bash configure && make -j16')