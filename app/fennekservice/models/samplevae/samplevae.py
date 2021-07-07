from fennekservice.models.model import FennekModel
from fennekservice.models.samplevae.tool_class import SoundSampleTool

import os


class SampleVAEModel(FennekModel):
    def __init__(self, model_id: str = 'model_snare2', library_dir: str = '/content/drive/MyDrive/Samples'):
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
