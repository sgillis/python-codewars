from kyu7_complementary_dna import DNA_strand


def test_DNA_strand():
    assert "TAACG" == DNA_strand("ATTGC")
    assert "CATA" == DNA_strand("GTAT")
