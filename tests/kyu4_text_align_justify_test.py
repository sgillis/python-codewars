from kyu4_text_align_justify import justify, add_spaces, clever_justify


def test_add_spaces():
    assert ['123', '  ', '45'] == add_spaces(['123', '45'], 7)


def test_justify():
    assert '123  45\n6' == justify('123 45 6', 7)
    assert expected_text() == justify(input_text(), 30)


def test_clever_justify():
    assert expected_text() == clever_justify(input_text(), 30)


def input_text():
    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In \
quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit \
tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus \
tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet \
lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. \
Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies \
a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis \
rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus \
dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio \
porta lacus, ut elementum justo nulla et dolor."""


def expected_text():
    return """\
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor."""
