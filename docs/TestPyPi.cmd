python -m build
python -m twine upload --repository testpypi dist/*
python -m twine upload --repository pypi dist/*
pip install -i https://test.pypi.org/simple/ DE-DataBaseConnect==0.0.95.3 # test.pypi
pip install -i DE-DataBaseConnect==0.0.95.3 # Pypi


python -m pip install --upgrade pip

