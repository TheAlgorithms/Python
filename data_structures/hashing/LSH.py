"""
This program aims to detect plagiarism using Locality Sensitive Hahsing(LSH)
Process:
    - shingling: converting documents into set of tokens. each token is called 
        as shingle which is a sequence of characters present in file. This process
        generates a sparse incidence matrix
    - minhashing: as incidence matrix is sparse, this step aims to reduce the 
        size of matrix by producing signature for each document present in the 
        incidence matrix
    - lsh: dividing signature matrix into horizontal bands and applying hash
        functions on them to determing which documents fall in same bucket
NOTE: if pickle(binary) files exist for each operation, they will be used 
    instead of generating them again(to save time). rename or delete the file
    to start afresh.
"""

import time, os
import shingling
import minhashing
import lsh
import statistics

def startLSH():
    print("\n*** Plagiarism detection using LSH ***\n")

    # step 1: shingling
    timer_start = time.time()   # start timer
    folderpath = "corpus"       # path to corpus
    extension=".txt"            # specified extensions to read. Set to None to ignore extension
    shingle_size = 4            # size of shingle: 8-12 is reommended
    shingle_matrix, files = shingling.get_shingle_matrix(folderpath, shingle_size, extension)
    print(shingle_matrix.shape)
    print(f"Time taken for shingling: {time.time()-timer_start}")

    # step 2: min-hashing
    start_time = time.time()    # start timer
    no_of_hash_functions = 50   # specify no of hash functions for signature matrix
    signature_matrix = minhashing.generate_signature_matrix(shingle_matrix, no_of_hash_functions)
    print(f"Time taken for minhashing: {time.time()-start_time}")

    # step 3: LSH(Locality sensitive hashing)
    start_time = time.time()    # start timer
    r = 2
    buckets_list = lsh.get_bucket_list(signature_matrix, r)
    print(f"Time taken for lsh: {time.time()-start_time}")

    # preprocessing done. ask file from user to check plagiarism
    sim_type = "jaccard"
    while True:
        test_file = input("Enter path of file: ")
        if test_file == "EXIT":
            break;
        if not os.path.exists(test_file):
            print(">> The given path does not exist.")
            continue
        for name, num in files:
            if test_file == name:
                test_file = int(num)
        # test_file = int(input("Enter path of file: "))
        threshold = float(input("Enter threshold: "))

        print(f"Given file: {statistics.get_file_name(test_file, files)}")
        similar_docs = lsh.find_similar_docs(test_file, buckets_list, signature_matrix, r)
        output = statistics.compute_similarity(test_file, similar_docs, shingle_matrix, sim_type)

        for file_id, score in output:
            print(f"{statistics.get_file_name(file_id, files)}\t{score}")
        
        print(f"Precision: {statistics.precision(threshold, output)}")
        print(f"Recall: {statistics.recall(threshold, test_file, len(files), output, shingle_matrix, sim_type)}")

    print("\n*** End of Program ***\n")

if __name__ == "__main__":
    startLSH()