FROM ubuntu:18.04 as builder
 
RUN apt-get update \
   && DEBIAN_FRONTEND=noninteractive apt-get install -yq expect lsb-release sudo wget build-essential autoconf automake bison flex libssl-dev bc u-boot-tools \
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
WORKDIR /ti-processor-sdk-linux-am335x
COPY --from=builder /ti-processor-sdk-linux-am335x .
 
RUN apt-get update \
   && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
       autoconf \
       automake \
       bc \
       bison \
       build-essential \
       flex \
       libssl-dev \
       u-boot-tools \
   && rm -rf /var/lib/apt/lists/*
 
CMD ["make"]
