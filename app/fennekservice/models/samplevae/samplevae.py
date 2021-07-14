from fennekservice.models.model import FennekModel
from fennekservice.models.samplevae.tool_class import SoundSampleTool

import os


class SampleVAEModel(FennekModel):
#"fennekservice/models/samplevae/model_drum_classes/search_thing"
    def __init__(self, model_id: str = 'model_drum_classes', library_dir: str = "fennekservice/models/samplevae/model_drum_classes/search_thing"):

        super().__init__()
        try:
            real_path = os.path.realpath(__file__)
            dir_path = os.path.dirname(real_path)
            log_dir = os.path.join(dir_path, model_id)
            self.tool = SoundSampleTool(logdir=log_dir,
                                        library_dir=library_dir,
                                        library_segmentation=False)
        except:
            print("Could not load SampleVAE model")
            self.tool = None
            raise


    def find_similar(self, target_file, x=None, **kwargs):
        similar_files, onsets, distances = self.tool.find_similar(target_file, num_similar=5)
        print(target_file)
        print(similar_files)
        return similar_files

    def get_TSNE(self, x=None, **kwargs):
        return self.tool.get_TSNE()

    def forward(self, x=None, **kwargs):
        relative_file_path = "generated.wav"
        if x is not None:
            # TODO: use the input file and set the weights appropriately
            # also experiment with the variance
            audio_files = []
            weights = []
        else:
            audio_files = []
            weights = []

        print("Jetzt wird es generiert, in der forward methode")
        self.tool.generate(out_file=relative_file_path,
                           audio_files=audio_files,
                           weights=weights,
                           normalize_weights=True,
                           variance=0.0)

        with open(relative_file_path, "rb") as f:
            y = f.read()

        return y
