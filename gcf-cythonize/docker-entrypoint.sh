#! /bin/bash
 
/opt/python/cp38-cp38/bin/python setup.py bdist_wheel
auditwheel repair dist/*.whl
