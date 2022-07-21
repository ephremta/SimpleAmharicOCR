# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
from PIL import Image
# import cv2
import pytesseract
# import cv2
import pytesseract
import streamlit as st
from PIL import Image

# configuring parameters for tesseract
st.header('')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def load_image(image_file):
    img = Image.open(image_file)
    return img


def main():
    st.title("የአማርኛ ኦፕቲካል ካራክተር ሪኮኒሽን ሲስተም")
    menu = ["ምስል", "ፒዲኤፍ"]
    choice = st.sidebar.selectbox("ምስል ወይም ፒዲኤፍ ዶክመንት ይመረጡ", menu)

    if choice == "ምስል":
        st.markdown("""
        * **ምስልን ተቀብሎ ወደ ጽሁፍ ይቀይራል**
        ይህ ሲስተም ማኛውንም በኮምፕዩተር የተጻፉ የአማርኛ ዶክመንቶችን ወይም ምስሎችን በቀላሉ አርትዖት ማድረግ ወደ ሚያስችለን ቴክስት ወይም ወርድ ኮመንት ይቀይርልናል።  
        """)
        image_file = st.file_uploader("እባከወትን ቀጥሎ ያለውን በተን በመጫን የሚፈልጉትን ምስል ከማህደር ይምረጡ",
                                      type=["png", "jpg", "jpeg", "JPG", 'PNG', 'JPEG'])
        if image_file is not None:
            st.write("የመረጡት ምስል አጠቃላይ መረጃ የሚከተለውን ይመስላል")
            file_details = {"የፋይሉ ስም": image_file.name, "የፋይሉ አይነት": image_file.type,
                            "የሳይሉ መጠን": image_file.size}
            st.write(file_details)
            # To View Uploaded Image
            #st.image(load_image(image_file), width=250)
            im = Image.open(image_file)
            data = pytesseract.image_to_string(im, lang='amh')
            with open('converted_text_file.txt', 'w', encoding='utf-8') as file:
                file.write(data)
                st.subheader("ቀጥሎ ያለው ጽሁፍ ከምስሉ የተቀየረው ይዘት ነው!")
                st.text_area(label="", value=data, height=350)

            st.success(" የተቀየረው ጽሁፍ ወደ ማህደረወ ተቀምጧል! ")

    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        """ """


if __name__ == '__main__':
    main()
