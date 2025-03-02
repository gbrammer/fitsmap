import numpy as np
from astropy.io import fits

from fitsmap import convert

if __name__ == "__main__":

    convert.dir_to_map(
        "./tmp",
        out_dir="./tmp/web",
        min_zoom=1,
        cat_wcs_fits_file="./tmp/F200W.fits",
        exclude_predicate=lambda f: f.endswith(".fits"),
        catalog_delim=convert.MIXED_WHITESPACE_DELIMITER,
        task_procs=1,
        procs_per_task=1,
        image_engine=convert.IMG_ENGINE_PIL,
        rows_per_column=15,
    )
