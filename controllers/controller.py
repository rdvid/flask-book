import json
import os
import base64
import uuid

from flask import Response
from sendgrid import SendGridAPIClient, Attachment, FileType, FileContent, ContentId, Disposition, FileName
from sendgrid.helpers.mail import Mail


def send_email(book, title, author, kindle_email):
    """

    send a document through Sendgrid

    :param book: multiform/data file
    :param title: string
    :param author: string
    :param kindle_email: string
    :return: HttpResponse + Json status message


    """

    file_type = book.filename.split('.')[-1]

    book = base64.b64encode(book.read()).decode()

    book_attachment = Attachment()
    book_attachment.file_content = FileContent(book)
    book_attachment.file_type = FileType('application/epub+zip')
    book_attachment.file_name = FileName(f"{title} - {author}.{file_type}")
    book_attachment.disposition = Disposition('attachment')
    book_attachment.content_id = ContentId(f"{uuid.uuid4()}")

    if file_type == 'pdf':
        book_attachment.file_type = FileType('application/pdf')

    message = Mail(
        from_email=os.environ.get('EMAIL_SENDER'),
        to_emails=kindle_email,
        subject=f"New book: {title}",
        html_content=f"<strong>new book: {title} by {author}</strong>"
    )

    message.add_attachment(book_attachment)

    try:
        api_key = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(api_key)
        sg.send(message)
        data = {"message": "book send successfully :)"}
        return Response(status=201, content_type='application/vnd.api+json', response=json.dumps(data))
    except Exception as e:
        print(e)
        data = {"message": "oh-oh something bad happens :("}
        return Response(status=500, content_type='application/vnd.api+json', response=json.dumps(data))
