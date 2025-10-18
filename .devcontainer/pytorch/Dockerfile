# Use an official NVIDIA CUDA image with a specific CUDA version and OS (e.g., Ubuntu 20.04)
# Check NVIDIA NGC catalog for appropriate images (e.g., Pytorch, Tensorflow, or a base CUDA image)
FROM nvcr.io/nvidia/ai-workbench/pytorch:1.0.6

ENV PYTHONUNBUFFERED 1

# [Optional] Uncomment this section to install additional OS packages.
#RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends python3-pip

# Instala pacotes básicos e o pip
#RUN apt-get update && \
#    apt-get install -y --no-install-recommends python3-pip python3-venv && \
#    python3 -m pip install --upgrade pip setuptools wheel && \
#    rm -rf /var/lib/apt/lists/*


# Crie um novo usuário e grupo não-root (ex: 'vscode' or 'appuser' com UID/GID 1000)
#ARG USER_UID=1000
#ARG USER_GID=1000
#ARG USER_NAME=vscode

#RUN groupadd --gid $USER_GID $USER_NAME && \
#    useradd --uid $USER_UID --gid $USER_GID --shell /bin/bash --create-home $USER_NAME

# (Opcional) Defina o usuário padrão para futuras instruções RUN
# USER $USER_NAME

# Install Python packages from requirements.txt
COPY pytorch/requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Defina o diretório de trabalho principal e dê permissão ao novo usuário
WORKDIR /workspaces
#RUN chown -R $USER_NAME:$USER_GID /workspaces

# Crie um link simbólico para python3 como python
#RUN ln -s /usr/bin/python3 /usr/bin/python