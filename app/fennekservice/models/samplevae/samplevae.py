from fennekservice.models.model import FennekModel
from fennekservice.models.samplevae.tool_class import SoundSampleTool

import os


class SampleVAEModel(FennekModel):
#"fennekservice/models/samplevae/model_drum_classes/search_thing"
#/Users/Emrehan/frontend/ReactUI/backend/fennekservice/models/samplevae/origin_sample_library/All
#/Users/Emrehan/Documents/GitHub/SampleVAE_Train/origin_sample_library/Kick
#model_id: str = 'model_all2', instrument: str = "Similarity Search", library_dir: str = "fennekservice/models/samplevae", ae_variance: float = 0.0, selectedSound: str = ""
    def __init__(self, model_id: str = 'model_toms', instrument: str = "Toms", library_dir: str = "fennekservice/models/samplevae/model_toms", ae_variance: float = 0.0, selectedSound: str = ""):
        models = {"Kick": 'model_kick',
                  "Snare": 'model_snare',
                  "Conga": 'model_conga',
                  "Cowbell": 'model_cowbell',
                  "Crash": 'model_crash',
                  "Ride": 'model_ride',
                  "Rimshot": 'model_rimshot',
                  "Toms": 'model_toms',
                  "Clap": 'model_clap',
                  "Hihat": 'model_hihat',
                  "Similarity Search": 'model_all2'
                  }
        self.instrument = instrument
        self.model_id = models[instrument]
        real_path = os.path.realpath(__file__)
        dir_path = os.path.dirname(real_path)
        log_dir = os.path.join(dir_path, model_id)
        super().__init__()
        try:
            real_path = os.path.realpath(__file__)
            dir_path = os.path.dirname(real_path)
            log_dir = os.path.join(dir_path, model_id)
            print(selectedSound)




            print("Instrument Selected:")
            print(self.instrument)
            print(models[self.instrument])


            self.tool = SoundSampleTool(logdir=log_dir,
                                        library_dir=library_dir,
                                        library_segmentation=False)
            self.ae_variance = float(ae_variance)
            print("AE_VARIANCE")
            print(ae_variance)
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

    def get_model_id(self):
        return self.model_id

    def get_instrument(self):
        return self.instrument

    def forward(self, x=None, selectedSound="", ae_variance=0.0, **kwargs):
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
                           variance=ae_variance,
                           selectedSound=selectedSound)

        with open(relative_file_path, "rb") as f:
            y = f.read()

        return y
