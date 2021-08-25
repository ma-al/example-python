# Summary
It is good to think about how others can run and understand your code:
- allows colleagues to run experiments on their own machines
- makes it easier for engineers to deploy your algorithms
- helps CSCRC legal team see and record any external software

It is recommended to use some form of abstraction/virtualisation, like `virtualenv`, `miniconda` or `docker`. What ever you choose, put instructions and configurations in here.

# Example
Usually, you install modules that you depend on for a specific platform (e.g., Linux, MacOS or Windows). For example, if you use `miniconda` and are on a Mac, you would have [this conda configuration](./conda-mac.yml).

```bash
cd example-python

# So others can re-create the environment
conda env create --file environments/conda-mac.yml

# In case some Python packages are not in conda
pip install -r environments/pip.txt
```