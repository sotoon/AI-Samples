# Python Samples

In order to use python samples, you need to generate the python classes from
your `.proto` file. Here we explain how.

> Here we assume you've read [the main Readme](./../README.md)

### Step 1: Install dependencies
Install `protoc` module:  
```shell script
python3 -m pip install grpcio grpcio-tools
```

### Step 2: Generate python files
Now you have to use this command to generate a pair of files from a `.proto`
file. Note that you have to replace `my_proto.proto` with your `.proto` file
address.
```shell script
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. my_proto.proto
```
This command generates two files in your working directory that end with
`_pb2.py` and `_pb2_grpc.py`. From now on, you only need these Python files, so
you can delete the `.proto` file.

### Step 3: Put the generated files in your project
You need to `import` these files in your python codes in order to use our
service, so you should add these files somewhere in your project, but since
the `*_pb2_grpc.py` file imports the `*_pb2.py` file, when you copy these
files into your project, make sure you have corrected the `import` statement.
We suggest you change the import statement into a relative import, so you can
freely move this pair in your project without worrying about the `import`.

### Step 4: Call the service using the generated files
For this, you can simply use the `grpc` module in Python, but we've included
some sample codes on our services to make it easier for you to use:
* [NLP / Spell Checker](./nlp/spell_checker/)

---
[Go Back](./../README.md)
