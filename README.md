```
virtualenv env2
source env2/bin/activate
pip install python-keyczar
python fault.py

deactivate
python3 -m venv env3
source env3/bin/activate
pip install python3-keyczar
python fault.py
```
https://github.com/google/keyczar/issues/214
