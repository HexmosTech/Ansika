FROM debian:bullseye-slim as base




RUN apt-get update -y \    
    && apt-get install --no-install-recommends -y python3.9 \
         pipenv \    
    && cd /code \    
    && pip install ansible==7.0.0 \
    && rm -rf /var/cache/apt/archives

WORKDIR /code

COPY ./ext.yml /code

COPY ./executor.py /code


RUN apt-get update -y \
    && apt-get install --no-install-recommends -y \
        python3.9-dev \
        build-essential \
        patchelf \
        ccache \
        clang \
        libfuse-dev \
        upx \
    && python3.9 -m pip install nuitka==1.7.5

RUN python3.9 -m nuitka \
        --onefile \
        --include-package-data=ansible:'*.py' \
        --include-package-data=ansible:'*.yml' \ 
        --include-data-files=/code/ext.yml=ext.yml \
        executor.py


