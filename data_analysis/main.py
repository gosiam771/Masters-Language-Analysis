import argparse
from data_analysis import load
from data_analysis import statistics
from data_analysis import analysis
from data_analysis import output
from data_analysis import plots

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--dictionary", type=str, required=True, help="Dictionary file")
    parser.add_argument("--dictionary-stats", action="store_true", help="Display dictionary statistics")
    parser.add_argument("--works", type=str, required=True, help="Comma separated list of works")
    parser.add_argument("--works-stats", action="store_true", help="Display works statistics")
    parser.add_argument("--no-words", action="store_true", help="Display words not found in the dictionary")

    parser.add_argument("--frequencies", type=int, help="Display N most frequent words for each work")

    parser.add_argument("--output", type=str, required=True, help="Output file")
    parser.add_argument("--results-dir", type=str,default="results", help="Directory where plots will be saved")
    args = parser.parse_args()

    open(args.output, "w", encoding="utf-8").close()
    dictionary_text = load.load_dictionary_text(args.dictionary)
    texts, text_sum = load.load_works(args.works)

    # statystyki słownika
    if args.dictionary_stats:
        stats = statistics.dictionary_stats(args.dictionary)
        output.save_results(args.output,
                            "========== DICTIONARY STATISTICS ==========")
        output.save_results(args.output,
                            stats)

    if args.works_stats:
        stats = statistics.works_stats(args.works)
        output.save_results(args.output,
                            "========== WORKS STATISTICS ==========")
        output.save_results(args.output,
                            stats)

    if args.no_words:
        brakujace = analysis.no_words(args.dictionary, args.works)
        output.save_results(args.output,
                            "========== WORDS NOT IN DICTIONARY ==========")
        output.save_results(args.output,
                            brakujace)
    if len(texts) >1:
        if args.frequencies:
            frequencies_result = analysis.files_frequencies(args.works, texts, args.frequencies)
            output.save_results(
                args.output,
                "========== MOST FREQUENT WORDS =========="
            )
            output.save_results(args.output, frequencies_result)
            similarity_result = analysis.similarity_comparison(args.works,texts, args.frequencies,args.results_dir)
            output.save_results(
                args.output,
                "========== SIMILARITY RESULTS =========="
            )
            output.save_results(args.output, similarity_result)
            plots.all_plots(args.works, texts, args.frequencies, args.results_dir)



import cProfile, pstats

cProfile.runctx("main()", globals(), locals(), "profile.prof")

with open("profile.txt", "w", encoding="utf-8") as f:
    stats = pstats.Stats("profile.prof", stream=f)
    stats.sort_stats("cumulative")
    stats.print_stats()