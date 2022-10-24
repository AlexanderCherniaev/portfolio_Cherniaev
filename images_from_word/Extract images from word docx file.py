#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install PyMuPDF


# In[118]:


from docx2pdf import convert
import fitz
import io
from PIL import Image

def img_from_docs(path_docx):
    convert(path_docx, path_docx[:-5]+"to_parse.pdf")
    # STEP 2
    # file path you want to extract images from
    file = path_docx[:-5]+"to_parse.pdf"
    print(file)

    # open the file
    pdf_file = fitz.open(file)

    # iterate over PDF pages
    for page_index in range(len(pdf_file))[1:]:
        # get the page itself
        page = pdf_file[page_index]
        # get image list
        image_list = page.get_images()
        # printing number of images found in this page
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
        else:
            print("[!] No images found on page", page_index)
        for image_index, img in enumerate(image_list, start=1):
            # get the XREF of the image
            xref = img[0]
            # extract the image bytes
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            # get the image extension
            image_ext = base_image["ext"]
            # load it to PIL
            image = Image.open(io.BytesIO(image_bytes))
            # save it to local disk
            image.save(open(f"C:/Users/user/Desktop/images_from_word/image{page_index+1}_{image_index}.{image_ext}", "wb"))


# In[119]:


img_from_docs("C:/Users/user/Downloads/Upwork description.docx")


# In[ ]:




