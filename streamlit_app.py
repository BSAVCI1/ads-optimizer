# .github/workflows/ci.yml
name: Test & Deploy

on:
  push:
    branches: [ main ]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Lint
        run: flake8 .
      - name: Run tests
        run: pytest

  deploy:
    needs: lint-and-test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Streamlit
        run: |
          streamlit run streamlit_app.py --server.headless true
        env:
          STREAMLIT_TOKEN: ${{ secrets.STREAMLIT_TOKEN }}
