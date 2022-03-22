#!/bin/bash

pdf=Financial_Report_for_ABC_Labs

pdftotext ${pdf}.pdf

grep -o "picoCTF{.*}" ${pdf}.txt

rm ${pdf}.txt
