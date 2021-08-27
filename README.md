# Summary
This is an an example Python code repository for members of Australia's [Cyber Security Cooperative Research Centre](https://cybersecuritycrc.org.au/). This was featured in the CSCRC seminar on "Software Best Practices" on 2021-08-27.

It is intended to:
- show expected structure of Python code
- encourage code reuse, sharing and safe storage
- ensure work is accessible for CSCRC legal team
- show how to use simple tools like `pylint`


# Installation
This module can be installed directly from GitHub.

```bash
# No username or password needed.
pip install git+https://github.com/ma-al/example-python.git

# note: only been tested on MacOS
```

Subsequently, the module will be downloaded and installed into your Python environment.

If successful, you should see:

```
Successfully built example-python
Installing collected packages: example-python
Successfully installed example-python-1.1.0
```


# Cloning
If you want to use this to start your own repo, simply clone it with below command:

```bash
git clone https://github.com/ma-al/example-python.git
```

Alternatively, use your favourite GUI Git tool, including:
- [GitHub Desktop](https://desktop.github.com)
- [SourceTree](https://www.sourcetreeapp.com)

Once cloned, be sure to [change the remote URL](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories#changing-a-remote-repositorys-url) to your own repository somewhere else.

It's probably easier for new users to either:
- [create a new repository from this template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/creating-a-repository-from-a-template), or
- [learn how to fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo




# Running
If installed directly via `pip`:
```bash
# just run in any folder
python -m example_python show-example
```

If you've cloned it:
```bash
cd example-python # go to repo root
python -m example_python show-example
```


# Tests
Researchers are encouraged to implement tests for their code. For more details, please see [documentation in the tests folder](./tests/README.md)


# Code Style & Quality
Researchers should strive for code quality that matches industry and community standards. Doing so leads to better science outcomes and easier sharing of knowledge.

If commercialisation is a criteria, writing good code from the start leads to faster prototyping and outcomes.

```bash
cd example-python # go to repo root
pylint example_python

# if pylint is not found
pip install pylint
```

Above conducts a check locally on your machine, using the included [pylintrc file](./pylintrc).


# Credits
List credits or references here, if applicable


# People
For help, please contact:
- [Kerrie Jackson](mailto:kerrie.jackson@cybersecuritycrc.org.au)
- [Mahathir Almashor](mailto:mahathir.almashor@data61.csiro.au)
