from synthetic_text_gen import SyntheticText
import os
import sys

'''Creates clean_fonts.csv
'''

if __name__ == "__main__":
    try:
        font_dir = sys.argv[1]
    except IndexError:
        font_dir = "./data/fonts"
    st = SyntheticText(font_dir, None)
    st.cleanFonts(os.path.join(font_dir, 'clean_fonts.csv'))
    print('created clean fonts file: clean_fonts.csv')
