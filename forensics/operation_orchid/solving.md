file image

calc offset via sector * sector size

mkdir test

mount image
`sudo mount -o loop,ro,offset=210763776 disk.flag.img test`

find for *flag*

look at history file from root

> get the openssl encryption

decrypt flag.txt

`openssl aes256 -d -in root/flag.txt.enc -k unbreakablepassword1234567`
