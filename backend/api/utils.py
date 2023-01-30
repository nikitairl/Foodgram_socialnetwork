from django.http import HttpResponse

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

BEGIN_POSITION_X = 40


def canvas_method(dictionary):
    """
    Метод сохранения списка покупок в формате PDF.
    """
    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = 'attachment; \
    filename = "shopping_cart.pdf"'
    begin_position_x, begin_position_y = 40, 650
    sheet = canvas.Canvas(response, pagesize=A4)
    pdfmetrics.registerFont(TTFont('BebasNeue-Book',
                                   'data/BebasNeue-Book.ttf'))
    sheet.setFont('BebasNeue-Book', 50)
    sheet.setTitle('Список покупок')
    sheet.drawString(begin_position_x,
                     begin_position_y + 40, 'Список покупок: ')
    sheet.setFont('BebasNeue-Book', 24)
    for number, item in enumerate(dictionary, start=1):
        if begin_position_y < 100:
            begin_position_y = 700
            sheet.showPage()
            sheet.setFont('BebasNeue-Book', 24)
        sheet.drawString(
            begin_position_x,
            begin_position_y,
            f'{number}.  {item["ingredient__name"]} - '
            f'{item["ingredient_total"]}'
            f' {item["ingredient__measurement_unit"]}'
        )
        begin_position_y -= 30
    sheet.showPage()
    sheet.save()
    return response
