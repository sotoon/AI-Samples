# Spell Checker Sample

> We assume you've read the [Python's Readme](./../../)

The sample code has comments explaining each section. The `.proto` file is
included, so you can see the fields in `CorrectRequest` and `CorrectResponse`
classes as well as the description of the service.

For a demonstration, generate the `pb` files as explained in
[Python's Readme](./../), put them in this directory, fill in
the `token` header in `spell_checker.py`, and then run this:  
```shell script
python3 spell_checker.py
```  

You should see something like the following in the output. The response
structure is defined in the `.proto` file.  
```text
suggestions {
  suggestions {
    text: "helo worlde"
    probability: 1.0
  }
}

one sample result:  helle world
```  

If there's any problem, check the [FAQ](./../../FAQ.md) document.
