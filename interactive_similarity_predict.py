import traceback
from scipy import spatial

from common import common
from extractor import Extractor

SHOW_TOP_CONTEXTS = 10
MAX_PATH_LENGTH = 8
MAX_PATH_WIDTH = 2
JAR_PATH = 'JavaExtractor/JPredict/target/JavaExtractor-0.0.1-SNAPSHOT.jar'


class SimilarityChecker:
    exit_keywords = ['exit', 'quit', 'q']

    def __init__(self, config, model):
        model.predict([])
        self.model = model
        self.config = config
        self.path_extractor = Extractor(config,
                                        jar_path=JAR_PATH,
                                        max_path_length=MAX_PATH_LENGTH,
                                        max_path_width=MAX_PATH_WIDTH)

    def read_file(self, input_filename):
        with open(input_filename, 'r') as file:
            return file.readlines()

    def similarity(self,dataSetI,dataSetII):
        result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
        return dataSetI,dataSetII, result
        # return dataSetI,dataSetII

    def predict(self,input_filename):
        # input_filename = 'Input.java'
        print('Starting interactive prediction...')
        # while True:
        print(
            'Modify the file: "%s" and press any key when ready, or "q" / "quit" / "exit" to exit' % input_filename)
        user_input = input()
        if user_input.lower() in self.exit_keywords:
            print('Exiting...')
            return
        try:
            predict_lines, hash_to_string_dict = self.path_extractor.extract_paths(input_filename)
        except ValueError as e:
            print(e)
            # continue
        results, code_vectors = self.model.predict(predict_lines)
        prediction_results = common.parse_results(results, hash_to_string_dict, topk=SHOW_TOP_CONTEXTS)
        for i, method_prediction in enumerate(prediction_results):
            print('Original name:\t' + method_prediction.original_name)
            for name_prob_pair in method_prediction.predictions:
                print('\t(%f) predicted: %s' % (name_prob_pair['probability'], name_prob_pair['name']))

        # for j in enumerate(code_vectors):
        #     print('ulala')
        #     resultVector = code_vectors[j]
        # print('size of vector: '.join(map(str, len(code_vectors))))
        return code_vectors[0]


    def GetSimilarityOfInputFiles(self):
        file1 = 'Source.java'
        file2 = 'Target.java'
        file1Data = self.predict(file1)
        file2Data = self.predict(file2)
        file1Vector, file2Vector, sim = self.similarity(file1Data, file2Data)
        print('Source Vector: \n ')
        print(' '.join(map(str, file1Vector)))
        print('Target Vector: \n ')
        print(' '.join(map(str, file2Vector)))
        print('Similarity: \n ')
        print(sim)
