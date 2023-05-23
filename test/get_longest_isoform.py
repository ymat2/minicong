#! /usr/bin/env python3

import argparse
import os
import glob

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("-i", "--indir")
  parser.add_argument("-o", "--outdir")
  args = parser.parse_args()

  fasta = glob.glob(args.indir+"/*.fa")
  for f in fasta:
    file_name = f.split("/")[-1].replace(".all.fa", ".longest.fa")
    f = get_longest_seq(f)
    write_fasta(f, args.outdir+"/"+file_name)


def get_longest_seq(pth):
  seq_array = fasta2array(pth)
  dct = {}

  for sblst in seq_array:
    gn = sblst[0]
    seq = sblst[1]
    if gn not in dct:
      dct[gn] = seq
    else:
      dct[gn] = max(seq, dct[gn], key=len)

  return dct


def fasta2array(pth):
  lst = []

  with open(pth) as f:
    for line in f:
      if line[0] == ">":
        gene_id = line.split(" ")[3][5:]
        lst.append([gene_id, ""])
      else:
        lst[-1][1] += line.rstrip()

  return lst


def write_fasta(dct, pth):
  with open(pth, "w") as f:
    for k, v in dct.items():
      f.write(">"+k+"\n")
      f.write(v+"\n")


if __name__ == "__main__":
  main()
