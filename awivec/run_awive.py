import argparse
from awive.config import Config
from awive.correct_image import Formatter
from awive.loader import Loader, make_loader
from awive.otv import OTV

def run_otv(config_path: str, show_video=False, debug=0):
    """Basic example of OTV

    Processing for each frame
        1. Crop image using gcp.pixels parameter
        2. If enabled, lens correction using preprocessing.image_correction
        3. Orthorectification using relation gcp.pixels and gcp.real
        4. Pre crop
        5. Rotation
        6. Crop
        7. Convert to gray scale
    """
    config = Config.from_json(config_path)
    loader: Loader = make_loader(config.dataset)
    formatter = Formatter(config)
    image = loader.read()
    prev_gray = formatter.apply_distortion_correction(image)
    prev_gray = formatter.apply_roi_extraction(prev_gray)
    otv = OTV(config, prev_gray, debug)
    return otv.run(loader, formatter, show_video)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_path",
        help="Path to configuration file path",
    )
    parser.add_argument(
        '-v',
        '--show_video',
        action='store_true',
        help='Show video'
    )
    args = parser.parse_args()
    x = run_otv(
        config_path=args.config_path,
        show_video=args.show_video,
    )
    for key, value in x.items():
        print(f"{key}: velocity: {round(value['velocity'],4)}, count: {value['count']}")
