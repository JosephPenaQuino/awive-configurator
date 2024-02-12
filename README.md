# AWIVE Configurator
The AWIVE configurator is a software used to analyze images in order to
determine the configuration used for the [awive](https://github.com/JosephPenaQuino/adaptive-water-image-velocimetry-estimator)
project.

## Usage

Execute the commands below:

```
pyenv local 3.11.2
poetry install
poetry run python -m awivec.analyze_image config.example.json -P
```
