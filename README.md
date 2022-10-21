# Oblig3-Softwere-Engineering-og-testing

Oblig 3 - git og continuous integration

jeg opprettet dette repositoret og lastet opp oblig 2
for å settte opp GitHub Actions la jeg til en ny fil .github/workflows/tests.yml.
Derreter brukte jeg https://docs.github.com/en/actions for å skrive korrekt syntax for yml filen. 

yml koden:
```yml
name: runTests

on: [push]

jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.7", "3.8", "3.9"]
        
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Test with pytest
      run: |
        pip install pytest
        pip install pytest-cov
        pytest main_test.py        
```

denne actionen vil kjøre hver gang det er en push request
```yml
on: [push]
```
Lager alle envirementsa testene vil kjøre i. Dette vil da være ubuntu med python 3.7, 3.8, 3.9 og windows med python 3.7, 3.8, 3.9. Vil kjøre 6 tester
```yml
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ["3.7", "3.8", "3.9"]
```
sjekker ut repositoriet, så setter den opp python fra matrix 
```yml
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
```

Installerer alle dependencies fra requirements.txt
```yml
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
```

installerer pytest og kjører testene på filen main_test.py
```yml
    - name: Test with pytest
      run: |
        pip install pytest
        pip install pytest-cov
        pytest main_test.py        
```
