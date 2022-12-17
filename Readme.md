# Credit4You
## Environment Setup
**Install** conda environment
```sh
$ conda install -f c4y.yml
```
**Update** the environment with new packages/versions:
1. modify c4y.yml
2. run `conda env update`:
```sh
$ conda env update --name c4y --file c4y.yml --prune
```
**Use** environment:
Before working on the project always make sure you have the environment activated:
```sh
$ conda activate c4y
```
