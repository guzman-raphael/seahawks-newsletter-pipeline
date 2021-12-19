from collections import defaultdict
import os
import datajoint as dj 
from skimage import io, util

schema = dj.schema(dj.config['custom']['database.prefix'] + 'image')

# === Useful functions===
def get_image_paths():
    paths = dj.config.get('custom', {}).get('image_root_data_dir',None)
    return paths


@schema
class ImageInfo(dj.Manual):
    definition = """
    #Image information
    image_id   : varchar(24)  #name of image
    ---
    filepath   : varchar(50)  #image location relative to image_root_data_dir
    """


@schema
class Image(dj.Imported):
    definition = """
    #Image
    -> ImageInfo
    ---
    image  : longblob   #the image itself
    """

    def make(self,key):
        #to do join filepath and 
        dirname = get_image_paths()
        filepath = (ImageInfo & key).fetch1('filepath')
        full_file_path = os.path.join(dirname, filepath)
        image = io.imread(full_file_path)
        
        key['image'] = image
        self.insert1(key)


@schema
class TransformedImage(dj.Computed):
    definition = """
    #The transformed image
    -> Image
    ---
    transformed_image : longblob  #new image
    """
    def make(self,key):
        image = (Image & key).fetch1('image')
        inverted_image = util.invert(image)
        key['transformed_image'] = inverted_image
        self.insert1(key)
