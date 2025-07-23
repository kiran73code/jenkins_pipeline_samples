# Run tests with coverage report
pytest --cov=simple_python

# Run tests with coverage and generate HTML report
pytest --cov=simple_python --cov-report=html

# Run tests with coverage and generate XML report
pytest --cov=simple_python \                                                                                                                      4 ↵
  --cov-report=xml:test_reports/coverage.xml \
  --cov-report=html:test_reports/htmlcov \
  --junitxml=test_reports/test-results.xml