FROM debian:bullseye-20210902-slim as builder

LABEL maintainer="suresh@robotpajamas.com"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash=5.1-2+deb11u1 \
    bzip2=1.0.8-4 \
    ca-certificates=20210119 \
    tar=1.34+dfsg-1+deb11u1 \
    wget=1.21-1+deb11u1 \
    && rm -rf /var/lib/apt/lists/* \
    && wget --progress=dot:giga -O- https://developer.arm.com/-/media/Files/downloads/gnu-rm/10.3-2021.07/gcc-arm-none-eabi-10.3-2021.07-x86_64-linux.tar.bz2 | tar -xj
    
FROM debian:bullseye-20210902-slim
    
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends \
    bash=5.1-2+deb11u1 \
    ccache=4.2-1 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r armoire \
    && useradd --no-log-init -u 1000 -r -g armoire armothy

USER armothy
COPY --from=builder --chown=armothy:armoire /gcc-arm-none-eabi-10.3-2021.07 /gcc-arm

ENV CCACHE_DIR="/ccache"
ENV PATH="/gcc-arm/bin:$PATH"

ENV ARCH="arm"
ENV CROSS_COMPILE="ccache /gcc-arm/bin/arm-none-eabi-"

CMD ["bash"]
