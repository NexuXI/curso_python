from Orquestra.clases_orquestra import Orquestra, Guitarra, GuitarraElectrica, Piano, Tambor

orquestra1 = Orquestra()

guitara1 = Guitarra("Guitarra1", "Cuerda", 5)
guitarra_electrica1 = GuitarraElectrica("GuitarraElectrica1", "Cuerda", "5", 10)
piano1 = Piano("Piano1", "Cuerda", 88)
tambor1 = Tambor("Tambor1", "Percusion", 20)

orquestra1.crear_orquestra(guitara1, guitarra_electrica1, piano1, tambor1)

orquestra1.iniciar_concierto()
