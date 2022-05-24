def insert_init_documentType(apps, schema_editor):
    typeID = apps.get_model('User', 'TypeID')
    types = ['Cédula', 'Cédula Extrangeria','NIT', 'Tarjeta de Identidad']
    for i in types:
        typeID.objects.create(Description = i)

def undo_insert_documentType(apps, schema_editor):
    typeID = apps.get_model('User', 'TypeID')
    typeID.objects.all().delete()

#     migrations.RunPython(insert_init_documentType, reverse_code=undo_insert_documentType)