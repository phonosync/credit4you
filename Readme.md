# Credit4You
## Setup Environment
Install conda environment
```sh
$ conda install -f c4y.yml
```
Update the environment with new packages/versions:
* modify c4y.yml
* then update from file
```sh
$ conda env update --name c4y --file c4y.yml --prune
```
Before working on the project always make sure you have the environment activated:
```sh
$ conda activate c4y
```
