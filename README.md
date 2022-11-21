<div id="header" align="center">
  <img src="https://media.giphy.com/media/vzO0Vc8b2VBLi/giphy.gif" width="100" alt=""/>
</div>

<div id="badges">
  <a href="https://www.linkedin.com/in/sviatoslav-ivanov-66a490182/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</div>

<img src="https://komarev.com/ghpvc/?username=Svet-Svet&style=flat-square&color=blue" alt=""/>

<h1>
A Difference Calculator
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>


#### Hexlet tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/085cd76c08914e156852/maintainability)](https://codeclimate.com/github/Svet-Svet/python-project-lvl2/maintainability)
[![Actions Status](https://github.com/Svet-Svet/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Svet-Svet/python-project-lvl2/actions)
[![Github Actions Status](https://github.com/Svet-Svet/python-project-lvl2/workflows/Python%20CI/badge.svg)](https://github.com/Svet-Svet/python-project-lvl2/actions)

This is a CLI-utility for comparison of two JSON-files or two YAML-files. It`s educational project at Hexlet School of Online Education.

## How it works

This is comparison of two JSON-files:


[![asciicast](https://asciinema.org/a/vMXOwSBxAi2AglCo5Rgtj7eDm.svg)](https://asciinema.org/a/vMXOwSBxAi2AglCo5Rgtj7eDm)

This is comparison of two YAML-files:

[![asciicast](https://asciinema.org/a/z6GXRTCjT4tBGLcBGriBi1PKX.svg)](https://asciinema.org/a/z6GXRTCjT4tBGLcBGriBi1PKX)

This is comparison of two big files with recursive approach:

[![asciicast](https://asciinema.org/a/Qnm0IqofPxkpUl1nJ7ZvLed2E.svg)](https://asciinema.org/a/Qnm0IqofPxkpUl1nJ7ZvLed2E)

This is a comparison of two big files with plain formatter:

[![asciicast](https://asciinema.org/a/utiCdBTgWmqpqFi1pp22PC0ww.svg)](https://asciinema.org/a/utiCdBTgWmqpqFi1pp22PC0ww)


## Dependencies

- Python = "^3.9"
- pytest = "^7.1.2"
- PyYAML = "^6.0"
- flake8 = "^5.0.4"

## Installation:

**Use the package manager pip:**
```
pip install --user git+https://github.com/Svet-Svet/python-project-lvl2
```
**Or you can clone repository and use poetry:**
```
git clone https://github.com/Svet-Svet/python-project-lvl2
cd python-project-lvl2
make build
make package-install
```