def formatar_nome(nome):
    return nome.title()
  import unittest

def formatar_nome(nome):
    return nome.title()

class TestFormatarNome(unittest.TestCase):
    def test_formatar_nome_minusculo(self):
        self.assertEqual(formatar_nome("joão da silva"), "João Da Silva")
        
    def test_formatar_nome_maiusculo(self):
        self.assertEqual(formatar_nome("MARIA FERREIRA"), "Maria Ferreira")
        
    def test_formatar_nome_misto(self):
        self.assertEqual(formatar_nome("cArLos alBeRto"), "Carlos Alberto")
        
    def test_formatar_nome_com_acentos(self):
        self.assertEqual(formatar_nome("angélica pérez"), "Angélica Pérez")

unittest.main(argv=[''], exit=False)
