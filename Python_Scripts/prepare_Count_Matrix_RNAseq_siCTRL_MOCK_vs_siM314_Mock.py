import pandas as pd

#load txt files from featureCounts into tables
#txt files must be tab delimited with two columns; column 1 Gene column 2 counts aligned to that gene
#replace "count_files/*.txt" with /path/to/countfile.txt if using a different countfile
CTRL_MOCK_rep1 = pd.read_table("count_files/CTRL1_MOCK_RNAseq_genc21_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
CTRL_MOCK_rep2 = pd.read_table("count_files/CTRL2_MOCK_RNAseq_genc21_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
CTRL_MOCK_rep3 = pd.read_table("count_files/CTRL3_MOCK_RNAseq_genc21_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
M314_MOCK_rep1 = pd.read_table("count_files/M314_1_MOCK_RNAseq_genc21_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
M314_MOCK_rep2 = pd.read_table("count_files/M314_2_MOCK_RNAseq_genc21_counts_cut.txt", names=['Genes_ID', 'number_fragments'])
M314_MOCK_rep3 = pd.read_table("count_files/M314_3_MOCK_RNAseq_genc21_counts_cut.txt", names=['Genes_ID', 'number_fragments'])

#turn tables into dictionaries
CTRL_MOCK_rep1_dict = CTRL_MOCK_rep1.set_index('Genes_ID')['number_fragments'].to_dict()
CTRL_MOCK_rep2_dict = CTRL_MOCK_rep2.set_index('Genes_ID')['number_fragments'].to_dict()
CTRL_MOCK_rep3_dict = CTRL_MOCK_rep3.set_index('Genes_ID')['number_fragments'].to_dict()

M314_MOCK_rep1_dict = M314_MOCK_rep1.set_index('Genes_ID')['number_fragments'].to_dict()
M314_MOCK_rep2_dict = M314_MOCK_rep2.set_index('Genes_ID')['number_fragments'].to_dict()
M314_MOCK_rep3_dict = M314_MOCK_rep3.set_index('Genes_ID')['number_fragments'].to_dict()

#create a list of Genes in the featureCounts textfiles
Genes = []
for key in CTRL_MOCK_rep1_dict.keys():
    Genes.append(key)

#print out the gene name, and the count corresponding to that gene from each replicate's dictionary
#store the output of the python script as a text file to make up the count matrix
for gene in Genes:
    a = CTRL_MOCK_rep1_dict[gene]
    b = CTRL_MOCK_rep2_dict[gene]
    c = CTRL_MOCK_rep3_dict[gene]
    d = M314_MOCK_rep1_dict[gene]
    e = M314_MOCK_rep2_dict[gene]
    f = M314_MOCK_rep3_dict[gene]
    print(f"{gene}\t{a}\t{b}\t{c}\t{d}\t{e}\t{f}")
