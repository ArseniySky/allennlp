import json
from allennlp.common.params import Params
from allennlp.training.util import make_vocab_from_params

# Path to your existing training config.
CONFIG_PATH = "test_fixtures/vilbert_vqa/experiment_from_huggingface.jsonnet"

params_overrides = {
    "dataset_reader": {
        "skip_image_feature_extraction": True,
    },
    "vocabulary": {
        "min_count": {"answers": 9},
    },
}
params_overrides = json.dumps(params_overrides)
params = Params.from_file(params_file=CONFIG_PATH, params_overrides=params_overrides)

# This will produce a folder `vocabulary` in the current directory.
make_vocab_from_params(params, "./test_fixtures/data/vqav2/")
# Turn it into an archive from the command line with:
# cd ./test_fixtures/data/vqav2/vocabulary && tar -czvf vocab.tar.gz .
