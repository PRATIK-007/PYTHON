
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.platypus import TableStyle

# List of Lists
data = [
    ['Employee_ID ', 'Company', 'Salary ', ' Post' ],
    ['EmP_5', 'HaldiRam', '10000', 'Manager'],
    ['EmP_7', 'Balaji', ' 75000', 'Assistant Manager']
    
]
fileName = 'pdfTable.pdf'
pdf = SimpleDocTemplate(fileName,pagesize=letter)
table = Table(data)
style = TableStyle([
    ('BACKGROUND', (0,0), (3,0),colors.white),
    ('TEXTCOLOR',(0,0),(-1,0),colors.greenyellow),

    ('ALIGN',(0,0),(-1,-1),'CENTER'),

    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 14),

    ('BOTTOMPADDING', (0,0), (-1,0), 12),

    ('BACKGROUND',(0,1),(-1,-1),colors.beige),

    ('BOX',(0,0),(-1,-1),2,colors.black),
  #  ('LINEBEFORE',(2,1),(2,-1),6,colors.red),
  #  ('LINEABOVE',(0,2),(-1,2),4,colors.green),
    ('GRID',(0,0),(-1,-1),2,colors.black),
    ]
)
table.setStyle(style)

elems = []
elems.append(table)

pdf.build(elems)