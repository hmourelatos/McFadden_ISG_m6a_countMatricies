# McFadden_ISG_m6a_countMatricies

Dependencies: Pandas v 1.1.0

**Script overview:**

1. prepare_Count_Matrix_RIBOseq_IFN_siCTRL_vs_siM314.py:
    *used to generate a countMatrix of read fragments aligned to each gene from the RIBOseq alignemnts of 
    *four siCTRL IFN treated replicates and four siMettl3/14 IFN treated replicates

2. prepare_Count_Matrix_RNAseq_siCTRL_IFN_vs_siM314_IFN.py:
    -used to generate a countMatrix of read fragments aligned to each gene from the RNAseq alignemnts of
    -three siCTRL IFN treated replicates and three siMettl3/14 IFN treated replicates

3. prepare_Count_Matrix_RNAseq_siCTRL_MOCK_vs_siCTRL_IFN.py:
    -used to generate a countMatrix of read fragments aligned to each gene from the RNAseq alignemnts of three siCTRL MOCK treated replicates 
    -and three siMettl3/14 IFN treated replicates

4. prepare_Count_Matrix_RNAseq_siCTRL_MOCK_vs_siM314_Mock.py:
    -used to generate a countMatrix of read fragments aligned to each gene from the RNAseq alignemnts of
    -three siCTRL MOCK treated replicates and three siMettl3/14 Mock treated replicates
  
  
 
  
**Outputs of each python script were stored as a text file to make up the respective analysis's count matrix**

**All text files containing gene and featureCounts raw counts aligned to each gene are in the McFadden_ISG_m6a_countMatricies/Python_Scripts/count_files**
