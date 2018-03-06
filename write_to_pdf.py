from fpdf import FPDF

# pdf = FPDF()
# pdf.add_page()
# pdf.set_xy(0, 0)
# pdf.set_font('arial', 'B', 13.0)
# pdf.cell(ln=0, h=5.0, align='L', w=0, txt="Hello", border=0)
# pdf.output('test.pdf', 'F')
#
# from fpdf import Template
#
# #this will define the ELEMENTS that will compose the template.
# elements = [
#     { 'name': 'company_logo', 'type': 'I', 'x1': 20.0, 'y1': 17.0, 'x2': 78.0, 'y2': 30.0, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo', 'priority': 2, },
#     { 'name': 'company_name', 'type': 'T', 'x1': 17.0, 'y1': 32.5, 'x2': 115.0, 'y2': 37.5, 'font': 'Arial', 'size': 12.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
#     { 'name': 'box', 'type': 'B', 'x1': 15.0, 'y1': 15.0, 'x2': 185.0, 'y2': 260.0, 'font': 'Arial', 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 0, },
#     { 'name': 'box_x', 'type': 'B', 'x1': 95.0, 'y1': 15.0, 'x2': 105.0, 'y2': 25.0, 'font': 'Arial', 'size': 0.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 2, },
#     { 'name': 'line1', 'type': 'L', 'x1': 100.0, 'y1': 25.0, 'x2': 100.0, 'y2': 57.0, 'font': 'Arial', 'size': 0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': None, 'priority': 3, },
#     { 'name': 'barcode', 'type': 'BC', 'x1': 20.0, 'y1': 246.5, 'x2': 140.0, 'y2': 254.0, 'font': 'Interleaved 2of5 NT', 'size': 0.75, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '200000000001000159053338016581200810081', 'priority': 3, },
# ]
#
# #here we instantiate the template and define the HEADER
# f = Template(format="A4", elements=elements,
#              title="Sample Invoice")
# f.add_page()
#
# #we FILL some of the fields of the template with the information we want
# #note we access the elements treating the template instance as a "dict"
# f["company_name"] = "Sample Company"
# f["company_logo"] = "pyfpdf/tutorial/logo.png"
#
# #and now we render the page
# f.render("./template.pdf")

# def report():
#     response.title = "web2py sample report"
#
#     # include a google chart (download it dynamically!)
#     url = "http://chart.apis.google.com/chart?cht=p3&chd=t:60,40&chs=500x200&chl=Hello|World&.png"
#     chart = IMG(_src=url, _width="250", _height="100")
#
#     # create a small table with some data:
#     rows = [THEAD(TR(TH("Key", _width="70%"), TH("Value", _width="30%"))),
#             TBODY(TR(TD("Hello"), TD("60")),
#                   TR(TD("World"), TD("40")))]
#     table = TABLE(*rows, _border="0", _align="center", _width="50%")
#
#     if request.extension == "pdf":
#         from gluon.contrib.pyfpdf import FPDF, HTMLMixin
#
#         # create a custom class with the required functionality
#         class MyFPDF(FPDF, HTMLMixin):
#             def header(self):
#                 "hook to draw custom page header (logo and title)"
#                 logo = os.path.join(request.env.web2py_path, "gluon", "contrib", "pyfpdf", "tutorial", "logo_pb.png")
#                 self.image(logo, 10, 8, 33)
#                 self.set_font('Arial', 'B', 15)
#                 self.cell(65) # padding
#                 self.cell(60, 10, response.title, 1, 0, 'C')
#                 self.ln(20)
#
#             def footer(self):
#                 "hook to draw custom page footer (printing page numbers)"
#                 self.set_y(-15)
#                 self.set_font('Arial', 'I', 8)
#                 txt = 'Page %s of %s' % (self.page_no(), self.alias_nb_pages())
#                 self.cell(0, 10, txt, 0, 0, 'C')
#
#         pdf = MyFPDF()
#         # create a page and serialize/render HTML objects
#         pdf.add_page()
#         pdf.write_html(str(XML(table, sanitize=False)))
#         pdf.write_html(str(XML(CENTER(chart), sanitize=False)))
#         # prepare PDF to download:
#         response.headers['Content-Type'] = 'application/pdf'
#         return pdf.output(dest='S')
#     else:
#         # normal html view:
#         return dict(chart=chart, table=table)