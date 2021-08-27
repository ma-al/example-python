# Summary
It is good to think about how others can run and understand your code:
- allows colleagues to run experiments on their own machines
- makes it easier for engineers to deploy your algorithms
- helps CSCRC legal team see and record any external software

It is recommended to use some form of abstraction/virtualisation, like `virtualenv`, `miniconda` or `docker`. What ever you choose, put instructions and configurations in here.

For example, if you use `miniconda` and are on a Mac, you would have [this conda configuration](./conda-mac.yml).


# Get Installed Packages (Conda)
If using `conda`, you can get a list of explicitly installed packages by doing:
```bash
conda env export --from-history
```

Which will show what you've explicitly installed (i.e., via `conda install ...`):
```yaml
name: example-python
channels:
  - defaults
dependencies:
  - python=3.9
  - pyyaml
  - pylint
  - pytest
  - jupyter
prefix: /Users/XXXX/miniconda3/envs/example-python # can delete this line (not needed)
```

You can also see what you explicitly installed via `pip install` within a conda environment:
```bash
conda list | grep pypi
```

Which would give you something like:
```
appdirs                   1.4.4                    pypi_0    pypi
filelock                  3.0.12                   pypi_0    pypi
idna                      3.2                      pypi_0    pypi
uritools                  3.0.2                    pypi_0    pypi
urlextract                1.3.0                    pypi_0    pypi
```

# Recreating Environments
Once you have your conda and pip requirements, your environment can be recreated on other machines.

```bash
cd example-python

# So others can re-create the environment
conda env create --file environments/conda-mac.yml

# In case some Python packages are not in conda
pip install -r environments/pip.txt
```

