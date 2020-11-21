FROM ubuntu:18.04 as builder

LABEL maintainer="suresh@robotpajamas.com"

SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

# hadolint ignore=DL3008,DL3015
RUN apt-get update \
   && apt-get install -y -qq expect lsb-release sudo wget build-essential autoconf automake bison flex libssl-dev bc u-boot-tools \
   && rm -rf /var/lib/apt/lists/*

WORKDIR /ti-processor-sdk-linux-am335x

RUN wget https://software-dl.ti.com/processor-sdk-linux/esd/AM335X/latest/exports/ti-processor-sdk-linux-am335x-evm-06.03.00.106-Linux-x86-Install.bin
RUN chmod +x ./ti-processor-sdk-linux-am335x-evm-06.03.00.106-Linux-x86-Install.bin
RUN ./ti-processor-sdk-linux-am335x-evm-06.03.00.106-Linux-x86-Install.bin --mode unattended --prefix .
RUN rm ./ti-processor-sdk-linux-am335x-evm-06.03.00.106-Linux-x86-Install.bin
COPY ./prompts.sh .
RUN chmod +x ./prompts.sh
RUN sudo ./prompts.sh && sudo ./prompts.sh
RUN rm ./prompts.sh


FROM ubuntu:18.04

SHELL ["/bin/bash", "-c"]
ARG DEBIAN_FRONTEND=non-interactive

# hadolint ignore=DL3008
RUN apt-get update \
   && apt-get install -y -qq --no-install-recommends \
      autoconf \
      automake \
      bc \
      bison \
      build-essential \
      flex \
      libssl-dev \
      u-boot-tools \
   && rm -rf /var/lib/apt/lists/* \
   && groupadd -r bitbakery \
   && useradd --no-log-init -u 1000 -r -g bitbakery bitbaker   

USER bitbaker
WORKDIR /ti-processor-sdk-linux-am335x
COPY --from=builder --chown=bitbaker:bitbakery /ti-processor-sdk-linux-am335x .

CMD ["make"]