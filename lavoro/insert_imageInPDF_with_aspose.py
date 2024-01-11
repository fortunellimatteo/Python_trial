import aspose.words as aw

doc = aw.Document("Input.pdf")
builder = aw.DocumentBuilder(doc)

# Insert image at the beginning of the document.
builder.move_to_document_start()
builder.insert_image("Image.png")
doc.update_page_layout()

doc.save("Output.pdf")