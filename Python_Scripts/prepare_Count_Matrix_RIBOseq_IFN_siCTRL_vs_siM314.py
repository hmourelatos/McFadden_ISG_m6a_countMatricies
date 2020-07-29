import pandas as pd

#load txt files from featureCounts into tables
#txt files must be tab delimited with two columns; column 1 Gene column 2 counts aligned to that gene
#replace "count_files/*.txt" with /path/to/countfile.txt if using a different countfile

RIBO_ctrl_rep1 = pd.read_table("count_files/CTRL_1_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
RIBO_test_rep1 = pd.read_table("count_files/M314_rep1_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
RIBO_ctrl_rep2 = pd.read_table("count_files/CTRL_2_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
RIBO_test_rep2 = pd.read_table("count_files/M314_rep2_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
RIBO_ctrl_rep3 = pd.read_table("count_files/CTRL_3_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
RIBO_test_rep3 = pd.read_table("count_files/M314_rep3_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
RIBO_ctrl_rep4 = pd.read_table("count_files/CTRL_4_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
RIBO_test_rep4 = pd.read_table("count_files/M314_rep4_genc21_RIBOseq_counts_cut.txt", names=['Genes_ID', 'number_fragments'])

#turn tables into dictionaries

RIBO_ctrl_rep1_dict= RIBO_ctrl_rep1.set_index('Genes_ID')['number_fragments'].to_dict()
RIBO_test_rep1_dict = RIBO_test_rep1.set_index('Genes_ID')['number_fragments'].to_dict()
RIBO_ctrl_rep2_dict= RIBO_ctrl_rep2.set_index('Genes_ID')['number_fragments'].to_dict()
RIBO_test_rep2_dict = RIBO_test_rep2.set_index('Genes_ID')['number_fragments'].to_dict()
RIBO_ctrl_rep3_dict= RIBO_ctrl_rep3.set_index('Genes_ID')['number_fragments'].to_dict()
RIBO_test_rep3_dict = RIBO_test_rep3.set_index('Genes_ID')['number_fragments'].to_dict()
RIBO_ctrl_rep4_dict= RIBO_ctrl_rep4.set_index('Genes_ID')['number_fragments'].to_dict()
RIBO_test_rep4_dict = RIBO_test_rep4.set_index('Genes_ID')['number_fragments'].to_dict()

#create a list of Genes in the featureCounts textfiles

Genes = []
for key in RIBO_ctrl_rep1_dict.keys():
        Genes.append(key)

#print out the gene name, and the count corresponding to that gene from each replicate's dictionary
#store the output of the python script as a text file to make up the count matrix

for gene in Genes:
    a = RIBO_ctrl_rep1_dict[gene]
    b = RIBO_ctrl_rep2_dict[gene]
    c = RIBO_ctrl_rep3_dict[gene]
    d = RIBO_ctrl_rep4_dict[gene]
    e = RIBO_test_rep1_dict[gene]
    f = RIBO_test_rep2_dict[gene]
    g = RIBO_test_rep3_dict[gene]
    h = RIBO_test_rep4_dict[gene]
    print(f"{gene}\t{a}\t{b}\t{c}\t{d}\t{e}\t{f}\t{g}\t{h}")
