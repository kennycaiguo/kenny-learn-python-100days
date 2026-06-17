# import PyPDF2 as pdf # the pic type pdf not working

# # reader = pdf.PdfReader("test-pic-type.pdf")
# reader = pdf.PdfReader("test-text-type.pdf")
# # print(reader) # <PyPDF2._reader.PdfReader object at 0x000001DFA7D6F7D0>
# # pages = reader.pages
# # print(pages[1].extract_text())
# for page in reader.pages:
#     print(page.extract_text())

# create a pdf file with reportlab
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

pdf_canvas = canvas.Canvas('./demo2.pdf', pagesize=A4)
width, height = A4

# 绘图
image = canvas.ImageReader('resources/couple.jpg')
pdf_canvas.drawImage(image, 20, height - 395, 250, 375)

# 显示当前页
pdf_canvas.showPage()

# 注册字体文件
pdfmetrics.registerFont(TTFont('Font1', 'resources/fonts/Vera.ttf'))
pdfmetrics.registerFont(TTFont('Font2', 'resources/fonts/hkposter.ttf'))

# 写字
pdf_canvas.setFont('Font2', 40)
pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
pdf_canvas.drawString(width // 2 - 120, height // 2, '你好，世界！')
pdf_canvas.setFont('Font1', 40)
pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
pdf_canvas.rotate(18)
pdf_canvas.drawString(250, 250, 'hello, world!')

# 保存
pdf_canvas.save()
