### Repo for CS350 Homework 4

Create a venv and install the requirements listed below to run pytest suite and benchmarking

Windows:

`python -m venv <venv_dir_name>`

    In cmd.exe:
    `venv\Scripts\activate.bat`

    In PowerShell:
    `venv\Scripts\Activate.ps1`

Unix:

`python3 -m venv <venv_dir name>`
`source <venv_dir_name>/bin/activate`


requirements (pip install):

`pytest`

`pytest-benchmark`

`pytest-timeout`


Recommend cloning this repo to a Unix environment such as `ada.cs.pdx.edu`.

Works on Windows too, but venv created differently

Run simple test cases in main with `make run` (unix) or `python3 min_sum.py` (windows).

Run comprehensive test suite with `make test` (unix) or `pytest -v` Optional: \[`--benchmark-histogram`\] (windows).
