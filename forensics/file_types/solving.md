 1. The file `Flag.pdf` isn't a pdf file
 1. If you check it with `file Flag.pdf`, you'll see, that it is a shell archive

```shell
Flag.pdf: shell archive text
```

 1. If you execute this archive, it will lead into some nested archives.
 1. Just keep extracting - renaming - extracting - renaming and in the end you will get the flag
 1. Finally you will get a text file with some hex strings... 
 1. CyberChef and the "From Hex" function will help you to get the flag.
