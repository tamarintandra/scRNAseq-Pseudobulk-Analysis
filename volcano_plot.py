import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

result_df = pd.read_csv('B_pseudobulk_result.tsv', sep='\t')
logfc_cutoff = 0
p_value_cutoff = 0.1
label_logfc_threshold = 2 # Only label genes with logFC >= 2

def volcano_plot(celltype_results, cell_type):
    plt.figure(figsize=(10, 6))
    # Plot non-significant points
    plt.scatter(
        celltype_results['logfoldchanges'][
            (celltype_results['pvals_adj'] >= p_value_cutoff) | (np.abs(celltype_results['logfoldchanges']) <= logfc_cutoff)
        ],
        -np.log10(celltype_results['pvals'][
            (celltype_results['pvals_adj'] >= p_value_cutoff) | (np.abs(celltype_results['logfoldchanges']) <= logfc_cutoff)
        ]),
        color='grey', alpha=0.5
    )

    # Plot significant points
    significant_points = celltype_results[
        (celltype_results['pvals_adj'] < p_value_cutoff) & (np.abs(celltype_results['logfoldchanges']) > logfc_cutoff)
    ]
    plt.scatter(
        significant_points['logfoldchanges'],
        -np.log10(significant_points['pvals']),
        color='red', alpha=0.7
    )

    # Annotate each significant point with the gene name
    for i, (gene_name, logfc) in enumerate(zip(significant_points['names'], significant_points['logfoldchanges'])):
        pval = significant_points['pvals'].iloc[i]

        # Check if p-value is non-zero before taking the logarithm
        logpval = -np.log10(pval) if pval > 0 else 0
        if np.abs(logfc) >= label_logfc_threshold:
            plt.text(
                logfc,
                logpval,
                gene_name,
                fontsize=8,
                color='black',
                ha='right' if i % 2 == 0 else 'left',  # Alternate the horizontal alignment for better readability
                va='bottom' if i % 2 == 0 else 'top'    # Alternate the vertical alignment for better readability
            )

    # Customize plot
    plt.axhline(y=-np.log10(p_value_cutoff), color='black', linestyle='--', linewidth=0.5)
    plt.axvline(x=logfc_cutoff, color='black', linestyle='--', linewidth=0.5)
    plt.axvline(x=-logfc_cutoff, color='black', linestyle='--', linewidth=0.5)
    plt.xlabel('Log2 Fold Change')
    plt.ylabel('-log10(P-value)')
    plt.title(f'{cell_type} Cell DE Genes in Healthy vs SLE')
    plt.grid(True)
    plt.savefig(f'{cell_type}_Volcano_Plot.png')

volcano_plot(result_df, 'B')