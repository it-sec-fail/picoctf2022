# GDB Test Drive

## Description
Can you get the flag?
Download this [binary](https://artifacts.picoctf.net/c/120/gdbme).
Here's the test drive instructions:
```shell
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```
