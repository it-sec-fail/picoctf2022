 1. Mounting the disk image (it is a msdos mbr partition... whole disk)
 1. Create temporary dir for mounting `mkdir test`
 1. Look into the partitiontable `fdisk -l <file>`
 1. After calculating the offset mount:

`mount -o loop,ro,offset=105906176 disk.img test`

 1. Look for ssh keyfiles

`find . -name '*id*'`

 1. Use the ssh key and try to login.

```shell
ssh -i root/.ssh/id_ed25519  -p 60303 ctf-player@saturn.picoctf.net
```

