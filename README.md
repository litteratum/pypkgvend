# Rootlib
The goal is to have "rootlib" distributed with vendored "submodules".

It works but "submodules.mylib" uses a relative import path which does not allow to test the "mylib" library separately.
