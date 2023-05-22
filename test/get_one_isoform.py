#! /usr/bin/env python3

import argparse

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--indir")
  parser.add_argument("-o", "--outdir")
  args = parser.parse_args()

  fasta = "test/"+args.indir+"/ncbi_dataset/data/"+args.indir+"/protein.faa"
  fasta = get_first_seq(fasta)

  write_fasta(fasta, args.outdir+"/"+args.indir+".fa")


def get_first_seq(pth):
  seq_dct = fasta2dict(pth)
  plot2gen = link_id(pth)
  gene_lst = []
  new_dct = {}

  for id, seq in seq_dct.items():
    gn = plot2gen[id]
    if gn not in gene_lst:
      new_dct[id] = seq
      gene_lst.append(gn)

  return new_dct


def fasta2dict(pth):
  dct = {}

  with open(pth) as f:
    t = ""
    for line in f:
      if line[0] == ">":
        prot_id = line.split(" ")[0][1:]
        t = prot_id
        dct[prot_id] = ""
      else:
        dct[t] += line.rstrip("\n")

  return dct


def link_id(pth):
  dct = {}

  with open(pth) as f:
    for line in f:
      if line[0] == ">":
        prot_id = line.split(" ")[0][1:]
        gene_dsc = "_".join(line.split(" ")[1:])
        if "isoform" in gene_dsc:
          gene_dsc = gene_dsc.split("_isoform")[0]
        else:
          gene_dsc = gene_dsc.split("_[")[0]
        dct[prot_id] = gene_dsc

  return dct


def write_fasta(dct, pth):
  with open(pth, "w") as f:
    for k, v in dct.items():
      f.write(">"+k+"\n")
      f.write(v+"\n")


if __name__ == "__main__":
  main()
