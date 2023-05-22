#! /bin/sh

for seq in GCF_001442555.1 GCF_003254395.2; do
  curl --globoff -OJX GET "https://api.ncbi.nlm.nih.gov/datasets/v1/genome/accession/"$seq"/download?exclude_sequence=True&include_annotation_type=PROT_FASTA&filename="$seq".zip" -H "Accept: application/zip"
  unzip $seq.zip -d test/$seq
  rm -r $seq.zip

  python3 test/get_one_isoform.py -i $seq -o data
done
