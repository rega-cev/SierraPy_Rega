import json
import itertools
import sys, argparse
from drugs import getAllDrugs, getEmptyDrugDict

def main(argv):
    inputfile = ''

    parser = argparse.ArgumentParser(description='Parse JSON file that was returned by sierrapy.')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-i', '--input', dest='input_file', help='Input file name', required=True)
    #parser.parse_args(['-h'])
    results = parser.parse_args(argv)
    input_file = results.input_file

    with open(input_file) as data_file:
        data = json.load(data_file)

    #Print header of csv file with predefined values
    ALLDrugs = getAllDrugs()
    sys.stdout.write("id,")
    for i in range(len(ALLDrugs)):
        sys.stdout.write(
        ALLDrugs[i] + "_SIR" + "," +
        ALLDrugs[i] + "_level" + "," +
        ALLDrugs[i] + "_score" + ","
        )
    sys.stdout.write("\n")

    # Loop over all the sequences
    for n in range(len(data)):
        empty_dict = getEmptyDrugDict()
        # Print all the drug_SIR, drug_level, drug_score
        # Loop over all the different genes (PR, RT, IN, ...)
        for i in range(len(data[n]["drugResistance"])):
            # Loop over each drug within each gene
            for j in range(len(data[n]["drugResistance"][i]["drugScores"])) :
                # Replace each [-,-,-] in the dict for each drug that we have in the json result
                empty_dict[str(data[n]["drugResistance"][i]["drugScores"][j]["drug"]["displayAbbr"])] = [str(data[n]["drugResistance"][i]["drugScores"][j]["SIR"]),
                str(data[n]["drugResistance"][i]["drugScores"][j]["level"]),str(data[n]["drugResistance"][i]["drugScores"][j]["score"])]

        print(data[n]["inputSequence"]["header"] + "," + ",".join(list(itertools.chain.from_iterable(empty_dict.values()))))

if __name__ == "__main__":
   main(sys.argv[1:])
