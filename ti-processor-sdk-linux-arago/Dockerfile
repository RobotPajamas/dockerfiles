FROM ubuntu:18.04 as builder
 
WORKDIR /ti-processor-sdk-linux-arago
 
RUN apt-get update \
   && apt-get install -yq git wget xz-utils
 
RUN wget https://developer.arm.com/-/media/Files/downloads/gnu-a/8.3-2019.03/binrel/gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz
RUN tar -Jxvf gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz
RUN rm gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf.tar.xz
 
RUN wget https://developer.arm.com/-/media/Files/downloads/gnu-a/8.3-2019.03/binrel/gcc-arm-8.3-2019.03-x86_64-aarch64-linux-gnu.tar.xz
RUN tar -Jxvf gcc-arm-8.3-2019.03-x86_64-aarch64-linux-gnu.tar.xz
RUN rm gcc-arm-8.3-2019.03-x86_64-aarch64-linux-gnu.tar.xz
 
RUN git clone git://arago-project.org/git/projects/oe-layersetup.git ./tisdk
WORKDIR /ti-processor-sdk-linux-arago/tisdk
 
 
FROM ubuntu:18.04
WORKDIR /ti-processor-sdk-linux-arago
COPY --from=builder /ti-processor-sdk-linux-arago .
 
# Pull required building packages and configure timezone and locale to avoid Python complaints
RUN apt-get update \
   && apt-get install -yq \
       build-essential \
       chrpath \
       cpio \
       diffstat \
       gawk \
       git \
       lib32ncurses5 \
       lib32z1 \
       libc6-i386 \
       libstdc++6-i386-cross \
       locales \
       python \
       python3 \
       texinfo \
       wget \
   && rm -rf /var/lib/apt/lists/* \
   && echo 'LANG="en_US.UTF-8"'>/etc/default/locale \
   && locale-gen en en_US en_US.UTF-8 \
   && dpkg-reconfigure --frontend=noninteractive locales \
   && update-locale LANG=en_US.UTF-8
 
# ENV LANG=en_US.UTF-8
# ENV LANGUAGE=en_US.UTF-8
# ENV LANG_ALL=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
 
# Required for bitbake compilation
ENV TOOLCHAIN_PATH_ARMV7=/ti-processor-sdk-linux-arago/gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf
ENV TOOLCHAIN_PATH_ARMV8=/ti-processor-sdk-linux-arago/gcc-arm-8.3-2019.03-x86_64-aarch64-linux-gnu
ENV MACHINE=am335x-evm
 
CMD ["bash"]
