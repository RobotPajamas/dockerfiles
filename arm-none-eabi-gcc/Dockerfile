FROM ubuntu:20.04

LABEL maintainer="suresh@robotpajamas.com"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
        bzip2 \
        ca-certificates \
        tar \
        wget \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r armoire \
    && useradd --no-log-init -u 1000 -r -g armoire armothy

WORKDIR /gcc
RUN wget -qO- https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2 | tar -xj

ENV PATH "/gcc/gcc-arm-none-eabi-9-2020-q2-update/bin:$PATH"
CMD ["bash"]

