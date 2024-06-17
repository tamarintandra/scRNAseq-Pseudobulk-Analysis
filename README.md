# scRNAseq-Pseudobulk-Analysis
Pseudobulk samples are created by aggregating or summing the read counts from a group of cells from the same individual for each cell type. This approach is important to avoid treating each cell as an independent sample in scRNA-seq analysis, which can lead to underestimated variance, small p-values, and an increased risk of false positives in statistical tests. 

The scRNA-seq data used in this analysis is sourced from [1] and is available for download [here](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE174188).

## Usage
1. Create an environment with all packages listed in ```requirements.txt``` installed.
2. Open the ```pseudobulk_diff_analysis.ipynb``` file in Google Colab or Jupyter Notebook.
3. Run all the cells in the notebook to observe.

## Volcano Plots
To generate volcano plots, you first need to obtain the TSV result file from **pseudobulk_diff_analysis.ipynb** and modify lines 5 and 60 in **volcano_plot.py** with the correct input path and cell type. The usage of the script is:

```
python volcano_plot.py
```

An example of the output is:

![B_Cell Volcano_Plot](https://github.com/tamarintandra/scRNAseq-Pseudobulk-Analysis/assets/140521132/9cf51683-0bb9-4b83-b17c-fd8c8da1caae)

## Citation
[1] Perez RK, Gordon MG, Subramaniam M, Kim MC, Hartoularos GC, Targ S, Sun Y, Ogorodnikov A, Bueno R, Lu A, Thompson M, Rappoport N, Dahl A, Lanata CM, Matloubian M, Maliskova L, Kwek SS, Li T, Slyper M, Waldman J, Dionne D, Rozenblatt-Rosen O, Fong L, Dall'Era M, Balliu B, Regev A, Yazdany J, Criswell LA, Zaitlen N, Ye CJ. Single-cell RNA-seq reveals cell type-specific molecular and genetic associations to lupus. Science. 2022 Apr 8;376(6589):eabf1970. doi: 10.1126/science.abf1970. Epub 2022 Apr 8. PMID: 35389781; PMCID: PMC9297655.
