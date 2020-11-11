FROM quay.io/pypa/manylinux1_x86_64
 
# RUN apt-get update \
#     && apt-get install -yq gcc patchelf unzip \
#     && rm -rf /var/lib/apt/lists/*
 
RUN /opt/python/cp38-cp38/bin/python -m pip install \
   # auditwheel \
   cython==3.0a6
 
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /entrypoint.sh
 
# Requires the user has mounted their working directory as a volume
WORKDIR /mnt/src
 
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/opt/python/cp38-cp38/bin/python"]
