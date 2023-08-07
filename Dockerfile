FROM debian:bullseye-slim as base




RUN apt-get update -y \    
    && apt-get install --no-install-recommends -y python3.9 \
         pipenv \       
    && pip install ansible==7.0.0 \
    && rm -rf /var/cache/apt/archives

WORKDIR /code

COPY ./one_installer.yml /code

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
        --clang \
        --include-package-data=ansible:'*.py' \
        --include-package-data=ansible:'*.yml' \ 
        --include-data-files=/code/one_installer.yml=one_installer.yml \
        executor.py


