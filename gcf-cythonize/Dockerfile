FROM quay.io/pypa/manylinux1_x86_64:2020-11-11-0f1f128

LABEL maintainer="suresh@robotpajamas.com"

RUN /opt/python/cp38-cp38/bin/python -m pip install cython==3.0a6 \
   && groupadd -r cythonite \
   && useradd -u 1000 -r -g cythonite cythonizer

USER cythonizer
COPY --chown=cythonizer:cythonite ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR /app

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/opt/python/cp38-cp38/bin/python"]
