from collections import defaultdict
import datajoint as dj 

schema = dj.schema(dj.config['custom']['database.prefix'] + 'image')

@schema
class ImageInfo(dj.Manual):
    definition = """
    #Image information
    image_id   : varchar(24)  #name of image
    ---
    filepath   : varchar(50)  #image location
    """

@schema
class Image(dj.Imported):
    definition = """
    #Image
    -> ImageInfo
    ---
    image: blob #the image itself
    """

    def make(self,key):
        print(key)

@schema
class TransformedImage(dj.Computed):
    definition = """
    #The transformed image
    -> Image
    ---
    transformed_image : blob  #new image
    """
