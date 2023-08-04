# How to reproduce

```bash
$ poetry install
$ poetry run app
```

## how to fix

in `pyproject.toml` - uncomment marked line `#pydantic = "^1.10.2" #uncomment this to fix`
```bash
$ rm poetry.lock
$ poetry install
$ poetry run app
```