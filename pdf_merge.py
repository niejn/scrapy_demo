# Merge two PDFs
'''from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(open("document1.pdf", "rb"))

# print how many pages input1 has:
print "document1.pdf has %d pages." % input1.getNumPages()

# add page 1 from input1 to output document, unchanged
output.addPage(input1.getPage(0))

# add page 2 from input1, but rotated clockwise 90 degrees
output.addPage(input1.getPage(1).rotateClockwise(90))

# add page 3 from input1, rotated the other way:
output.addPage(input1.getPage(2).rotateCounterClockwise(90))
# alt: output.addPage(input1.getPage(2).rotateClockwise(270))

# add page 4 from input1, but first add a watermark from another PDF:
page4 = input1.getPage(3)
watermark = PdfFileReader(open("watermark.pdf", "rb"))
page4.mergePage(watermark.getPage(0))
output.addPage(page4)


# add page 5 from input1, but crop it to half size:
page5 = input1.getPage(4)
page5.mediaBox.upperRight = (
    page5.mediaBox.getUpperRight_x() / 2,
    page5.mediaBox.getUpperRight_y() / 2
)
output.addPage(page5)

# add some Javascript to launch the print window on opening this PDF.
# the password dialog may prevent the print dialog from being shown,
# comment the the encription lines, if that's the case, to try this out
output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

# encrypt your new PDF and add a password
password = "secret"
output.encrypt(password)

# finally, write "output" to document-output.pdf
outputStream = file("PyPDF2-output.pdf", "wb")
output.write(outputStream)'''
# from PyPDF2 import PdfFileReader, PdfFileWriter
# from openpyxl.compat import file
#
# output = PdfFileWriter()
# pdfOne = PdfFileReader(file( "./histograms.pdf", "rb"))
# pdfTwo = PdfFileReader(file("./multipage_pdf.pdf", "rb"))
#
# output.addPage(pdfOne.getPage(0))
# output.addPage(pdfTwo.getPage(0))
#
# outputStream = file(r"output.pdf", "wb")
# output.write(outputStream)
# outputStream.close()
# from PyPDF2 import PdfFileWriter, PdfFileReader
#
# output = PdfFileWriter()
# input1 = PdfFileReader(open("document1.pdf", "rb"))
#
# # print how many pages input1 has:
# print("document1.pdf has %d pages." % input1.getNumPages())
#
# # add page 1 from input1 to output document, unchanged
# output.addPage(input1.getPage(0))
#
# # add page 2 from input1, but rotated clockwise 90 degrees
# output.addPage(input1.getPage(1).rotateClockwise(90))
#
# # add page 3 from input1, rotated the other way:
# output.addPage(input1.getPage(2).rotateCounterClockwise(90))
# # alt: output.addPage(input1.getPage(2).rotateClockwise(270))
#
# # add page 4 from input1, but first add a watermark from another PDF:
# page4 = input1.getPage(3)
# watermark = PdfFileReader(open("watermark.pdf", "rb"))
# page4.mergePage(watermark.getPage(0))
# output.addPage(page4)
#
#
# # add page 5 from input1, but crop it to half size:
# page5 = input1.getPage(4)
# page5.mediaBox.upperRight = (
#     page5.mediaBox.getUpperRight_x() / 2,
#     page5.mediaBox.getUpperRight_y() / 2
# )
# output.addPage(page5)
#
# # add some Javascript to launch the print window on opening this PDF.
# # the password dialog may prevent the print dialog from being shown,
# # comment the the encription lines, if that's the case, to try this out
# output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")
#
# # encrypt your new PDF and add a password
# password = "secret"
# output.encrypt(password)
#
# # finally, write "output" to document-output.pdf
# outputStream = file("PyPDF2-output.pdf", "wb")
# output.write(outputStream)

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import math


def main():
    if (len(sys.argv) != 3):
        print("usage: python 2-up.py input_file output_file")
        sys.exit(1)
    print("2-up input " + sys.argv[1])
    input1 = PdfFileReader(open(sys.argv[1], "rb"))
    output = PdfFileWriter()
    for iter in range(0, input1.getNumPages() - 1, 2):
        lhs = input1.getPage(iter)
        rhs = input1.getPage(iter + 1)
        lhs.mergeTranslatedPage(rhs, lhs.mediaBox.getUpperRight_x(), 0, True)
        output.addPage(lhs)
        print(str(iter) + " "),
        sys.stdout.flush()

    print("writing " + sys.argv[2])
    open("document1.pdf", "rb")
    # outputStream = file(sys.argv[2], "wb")
    outputStream = open(sys.argv[2], "wb")

    output.write(outputStream)
    print("done.")

def test():
    from PyPDF2 import PdfFileMerger

    merger = PdfFileMerger()

    input1 = open("multipage_pdf.pdf", "rb")
    input2 = open("foo2.pdf", "rb")
    input3 = open("my-fancy-document.pdf", "rb")

    # add the first 3 pages of input1 document to output
    merger.append(fileobj=input1, pages=(0, 3))

    # insert the first page of input2 into the output beginning after the second page
    merger.merge(position=2, fileobj=input2, pages=(0, 1))

    # append entire input3 document to the end of the output document
    merger.append(input3)

    # Write to an output PDF document
    output = open("document-output.pdf", "wb")
    merger.write(output)
    return

def test3():
    from PyPDF2 import PdfFileWriter, PdfFileReader

    output = PdfFileWriter()
    input1 = PdfFileReader(open("multipage_pdf.pdf", "rb"))

    # print how many pages input1 has:
    print("document1.pdf has %d pages." % input1.getNumPages())

    # add page 1 from input1 to output document, unchanged
    output.addPage(input1.getPage(0))

    # add page 2 from input1, but rotated clockwise 90 degrees
    output.addPage(input1.getPage(1).rotateClockwise(90))

    # add page 3 from input1, rotated the other way:
    output.addPage(input1.getPage(2).rotateCounterClockwise(90))
    # alt: output.addPage(input1.getPage(2).rotateClockwise(270))

    # add page 4 from input1, but first add a watermark from another PDF:
    page4 = input1.getPage(3)
    watermark = PdfFileReader(open("watermark.pdf", "rb"))
    page4.mergePage(watermark.getPage(0))
    output.addPage(page4)


    # add page 5 from input1, but crop it to half size:
    page5 = input1.getPage(4)
    page5.mediaBox.upperRight = (
        page5.mediaBox.getUpperRight_x() / 2,
        page5.mediaBox.getUpperRight_y() / 2
    )
    output.addPage(page5)

    # add some Javascript to launch the print window on opening this PDF.
    # the password dialog may prevent the print dialog from being shown,
    # comment the the encription lines, if that's the case, to try this out
    output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

    # encrypt your new PDF and add a password
    password = "secret"
    output.encrypt(password)

    # finally, write "output" to document-output.pdf
    outputStream = open("PyPDF2-output.pdf", "wb")
    output.write(outputStream)
    return 
if __name__ == "__main__":
    test()


