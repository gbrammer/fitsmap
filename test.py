import numpy as np
from astropy.io import fits

from fitsmap import convert

if __name__ == "__main__":

    convert.dir_to_map(
        "./tmp",
        out_dir="./tmp/web",
        zoom=None,
        cat_wcs_fits_file="./tmp/F200W.fits",
        exclude_predicate=lambda f: f.endswith(".fits"),
        task_procs=2,
        procs_per_task=2,
        image_engine=convert.IMG_ENGINE_PIL,
    )
