import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import AgglomerativeClustering
import numpy as np

def SLCA(part_machine_matrix_file='part_machine.csv', save_as='dendrogram.png'):
    X = np.genfromtxt(part_machine_matrix_file, delimiter=',')
    # X is an (m * n) matrix of 1's & 0's
    # m = No. of Machines
    # n = No. of Parts

    Z = linkage(X, 'single', 'jaccard')
    _ = dendrogram(Z, labels=np.arange(1, X.shape[0]+1))
    plt.title("Single Linkage Cluster Analysis")
    plt.xlabel("Machine")
    plt.ylabel("1 - Similarity Coefficient")
    plt.savefig(save_as)
    plt.show()

    for i in range(1, X.shape[0] + 1):
        clusters = AgglomerativeClustering(n_clusters=i, affinity='jaccard', linkage='single')
        clusters.fit(X)
        # clusters = fcluster(Z, i, criterion='distance')
        print(f"Number of clusters: {i}\tCluster Assignments: {clusters.labels_}")

SLCA()