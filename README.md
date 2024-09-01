# GenForm

This project is designed to generate synthetic forms intended for training and testing machine learning models. The synthetic forms mimic real forms with headers, text fields, and random data. This README provides instructions on how to set up and use the synthetic form generator.

## Prerequisites

Before you start, make sure you have the following installed on your machine:
- Python 3.6 or higher

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the required packages:**

   - PyTorch:
   ```bash
   python3 -m pip install torch
   ```

   - Scikit-Image:
   ```bash
   python3 -m pip install scikit-image
   ```

   - Transformers:
   ```bash
   python3 -m pip install transformers
   ```

   - Datasets:
   ```bash
   python3 -m pip install datasets
   ```

   - Matplotlib:
   ```bash
   python3 -m pip install matplotlib
   ```

   - Wget:
   ```bash
   python3 -m pip install wget
   ```

3. **Retrieve Fonts**

   This can be done in several ways:
   - **Manually:** Download fonts, move them to `data/fonts`, run:
     ```bash
     ls data/fonts > data/fonts/fonts.list
     ```
     then use `clean_fonts.py` to clean up the fonts;

   - **Using the scrape.sh script:** This script retrieves free fonts for commercial use from the 1001fonts.com website:
     ```bash
     bash synthetic_text_gen/scrape.sh
     ```
     You may need to filter out unreadable fonts if this script is used;

   - **Automating the cleaning of unreadable fonts (requires Tesseract):**
     ```bash
     pip install pytesseract
     pip install editdistance
     bash synthetic_text_gen/scrape_clean.sh
     ```

4. **Generate `gpt2_form_generation.json` using GPT-2:**

   - Use the `gpt_form.py` script to generate the `gpt2_form_generation.json` file.
   
   - Move the generated file to the `data` directory:
     ```bash
     mv gpt2_form_generation.json ./data/gpt2_form_generation.json
     ```

## Directory Structure

Ensure your project directory is structured as follows:

```
<repository-directory>/
├── data/
│   ├── fonts/
│   │   └── clean-fonts.csv
│   └── gpt2_form_generation.json
├── synth_form_dataset.py
├── genForm.py
├── other files...
├── gpt_form.py
└── README.md
```

## Running the Generator

Run the synthetic form generation script to generate the forms and save them in the specified directory:

```bash
python genForm.py [Number of samples to generate: 100] [Save images to disk: True] [Save images without a corresponding JSON: False] [Data directory: ./data] [Use masks: True]
```

Note: Ensure that the paths in the configuration are correctly defined according to your project directory structure.

## Configuration Parameters

Using the "config" parameter in the constructor of the `SynthFormDataset` class (in `genForm.py`), you can modify the generated forms.

- `'image_size'`: Default none — Image size.
- `'min_text_height'`: Default 8 — Minimum text size.
- `'max_text_height'`: Default 32 — Maximum text size.
- `'tables'`: Default 0.2 — Probability of adding a table to the form.
- `'augmentation'`: Default none — No effect.
- `'augment_shade'`: Default 1 — Add contrast/brightness distortions.
- `'additional_aug_params'`: Default {} — Other distortion parameters.
- `'batch_size'`: Not used (neutralized).
- `'questions'`: Default 1 — Number of question/answer pairs. Forced to 1 if `do_masks` is enabled.
- `'do_masks'`: Default 1 — Whether to use masks or not.
- `'max_qa_len_in'`: Default none — Maximum length of questions.
- `'max_qa_len_out'`: Default none — Maximum length of answers.
- `'max_qa_len'`: Replaces `max_qa_len_in` and `max_qa_len_out` if they are not defined.
- `'cased'`: Default True — Allow capitalization for questions/answers.
- `'color'`: Default False — Allow color in generated images (not implemented).
- `'rotation'`: Unused.
- `'crop_params'`: Default none — Parameters for transformations of the generated image.
- `'rescale_range'`: Scaling interval if the value is not explicitly given.
- `'rescale_to_crop_size_first'`: Default False — Explicit.
- `'rescale_to_crop_width_first'`: Default False — Explicit.
- `'rescale_to_crop_height_first'`: Default False — Explicit.
- `'cache_resized_images'`: Default False — Cache resized images.
- `'crop_to_q'`: Default False — Unused with this dataset.
- `'words'`: Default True — ?
- `'use_json'`: Default False — Level of use of the GPT-2 JSON. Options: False, 'test', 'only', 'fine-tune', 'streamlined', 'readtoo', 'readmore', or 'readevenmore'.
- `'shorten_text_in_json'`: Default False — Explicit.
- `'max_q_tokens'`: Default 20 — Max token length for questions.
- `'max_a_tokens'`: Default 800 — Max token length for answers.

Other parameters are unused.

## Credits

Special thanks to Brian Davis, Bryan Morse, Bryan Price, Chris Tensmeyer, Curtis Wigington, and Vlad Morariu for Dessurt (https://github.com/herobd/dessurt) and SyntheticTextGen (https://github.com/herobd/synthetic_text_gen/tree/master), from which this tool is a direct adaptation.

## Contributors

- **Achraf El Faiq**
- **Jade Manuel**
- **Tom Poget**
