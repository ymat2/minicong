#! /bin/sh

mkdir result


### blast: Dingo
makeblastdb -in data/Canis_lupus_dingo.ASM325472v1.pep.longest.fa \
  -out data/Canis_lupus_dingo.ASM325472v1.pep.longest.fa \
  -dbtype prot \
  -hash_index

blastp -outfmt "6 qseqid sseqid pident evalue" \
  -evalue 1e-4 \
  -db data/Canis_lupus_dingo.ASM325472v1.pep.longest.fa \
  -query data/human_amylase.fa \
  -out result/Canis_lupus_dingo.ASM325472v1.blastp


### blast: Dog
makeblastdb -in data/Canis_lupus_familiaris.ROS_Cfam_1.0.pep.longest.fa \
  -out data/Canis_lupus_familiaris.ROS_Cfam_1.0.pep.longest.fa \
  -dbtype prot \
  -hash_index

blastp -outfmt "6 qseqid sseqid pident evalue" \
  -evalue 1e-4 \
  -db data/Canis_lupus_familiaris.ROS_Cfam_1.0.pep.longest.fa \
  -query data/human_amylase.fa \
  -out result/Canis_lupus_familiaris.ROS_Cfam_1.0.blastp
