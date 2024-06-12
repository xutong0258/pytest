pip install pytest
cd .
pytest

pytest --junitxml=report.xml

pip install pytest-html
pytest --html=report/report.html
