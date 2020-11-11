FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -yq \
        bzip2 \
        wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /gcc
RUN wget -qO- https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2 | tar -xj

ENV PATH "/gcc/gcc-arm-none-eabi-9-2020-q2-update/bin:$PATH"
CMD ["bash"]
