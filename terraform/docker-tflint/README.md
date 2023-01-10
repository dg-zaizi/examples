# tflint

To build a Docker image that has [`tflint`](https://github.com/terraform-linters/tflint)
installed, run [`build.sh`](build.sh):

```bash
./build.sh
```

Some examples of running [`tflint`](https://github.com/terraform-linters/tflint)
with above Docker image (using [`run.sh`](run.sh)) are:

```bash
./run.sh "${PWD}"
./run.sh "${PWD}" --help
./run.sh "${PWD}" --version
./run.sh '/some/absolute/path'
./run.sh '/some/absolute/path' .
./run.sh '/some/absolute/path' foo.tf
./run.sh '/some/absolute/path' --color foo.tf
```
