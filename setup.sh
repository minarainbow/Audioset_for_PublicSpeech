#!/usr/bin/env bash

BIN_DIR="./bin"
CONDA_DIR="$BIN_DIR/miniconda"
CONDA_BIN_DIR="$CONDA_DIR/bin"

# Make bin folder
mkdir -p $BIN_DIR

# Install Anaconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O $BIN_DIR/Miniconda3-latest-Linux-x86_64.sh
bash $BIN_DIR/Miniconda3-latest-Linux-x86_64.sh -p $CONDA_DIR -b

# Install ffmpeg (with OpenSSL support)
wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz
tar xf ffmpeg-release-64bit-static.tar.xz
mv ffmpeg-3.3.4-64bit-static $BIN_DIR/ffmpeg

# Install conda dependencies
$CONDA_BIN_DIR/conda install -c conda-forge -y sox
$CONDA_BIN_DIR/conda install -c yaafe -y libflac
$CONDA_BIN_DIR/pip install --upgrade -r ./requirements.txt
