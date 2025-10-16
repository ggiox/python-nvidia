# Use an official NVIDIA CUDA image with a specific CUDA version and OS (e.g., Ubuntu 20.04)
# Check NVIDIA NGC catalog for appropriate images (e.g., Pytorch, Tensorflow, or a base CUDA image)
FROM nvcr.io/nvidia/pytorch:25.09-py3


# Install Python packages from requirements.txt
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Set the working directory
WORKDIR /usr/app