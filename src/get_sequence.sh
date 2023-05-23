#! /bin/sh

wget https://ftp.ensembl.org/pub/release-109/fasta/canis_lupus_familiaris/pep/Canis_lupus_familiaris.ROS_Cfam_1.0.pep.all.fa.gz
gunzip -d Canis_lupus_familiaris.ROS_Cfam_1.0.pep.all.fa.gz
mv Canis_lupus_familiaris.ROS_Cfam_1.0.pep.all.fa data/

wget https://ftp.ensembl.org/pub/release-109/fasta/canis_lupus_dingo/pep/Canis_lupus_dingo.ASM325472v1.pep.all.fa.gz
gunzip -d Canis_lupus_dingo.ASM325472v1.pep.all.fa.gz
mv Canis_lupus_dingo.ASM325472v1.pep.all.fa data/

python3 src/get_longest_isoform.py -i data -o data
