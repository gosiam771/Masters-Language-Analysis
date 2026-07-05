from data_analysis import analysis
import matplotlib.pyplot as plt
import os

def plots(files, texts,index,n,output_path,show=False):
    titles = []
    for j in files.split(","):
        titles.append(j.strip())
    plik0 = texts[index]

    similarity_results = []
    etykiety = []

    for i in range(len(texts)):
        if i != index:  # porównanie ze wszystkimi oprócz tego samego indeksu
            similarity_result = analysis.similarity(plik0, texts[i],n)
            similarity_results.append(similarity_result)
            etykiety.append(titles[i])

    plt.bar(etykiety, similarity_results)
    plt.title(f"Similarity to {titles[index]}")
    plt.ylabel("Similarity (0-100)")
    path = os.path.join(output_path, f'similarity_{index}.png')
    plt.savefig(path)

    if show:
        plt.show()

    plt.close()

def all_plots(files, texts,n,output_path,show=False):
    os.makedirs(output_path, exist_ok=True)
    for i in range(len(texts)):
        plots(files, texts,i,n,output_path,show)