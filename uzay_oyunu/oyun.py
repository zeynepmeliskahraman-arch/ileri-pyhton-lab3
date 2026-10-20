def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
  """Envanter durumuna göre metin döndürür."""
  parcalar = []
  if credits:
    parcalar.append("bol kredi")
  if engines:
    parcalar.append("güçlü motorlar")
  if copilot:
    parcalar.append("yetenekli bir pilot")

  if parcalar:
    return "Sende: " + ", ".join(parcalar)
  return ""


def hedef_menusu(hedefler: list[str]) -> str:
  """Numaralandırılmış hedef menüsü metni oluşturur."""
  menu = ["Nereye gitmek istersin?"]
  for i, hedef in enumerate(hedefler, 1):
    menu.append(f"[{i}] {hedef}")
  return "\n".join(menu)
def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
  """Envanter durumuna göre metin döndürür."""
  parcalar = []
  if credits:
    parcalar.append("bol kredi")
  if engines:
    parcalar.append("güçlü motorlar")
  if copilot:
    parcalar.append("yetenekli bir pilot")

  if parcalar:
    return "Sende: " + ", ".join(parcalar)
  return ""


def hedef_menusu(hedefler: list[str]) -> str:
  """Numaralandırılmış hedef menüsü metni oluşturur."""
  menu = ["Nereye gitmek istersin?"]
  for i, hedef in enumerate(hedefler, 1):
    menu.append(f"[{i}] {hedef}")
  return "\n".join(menu)

import json

def galaksi_kur(gezegenler: list[str], baglantilar: dict, baslangic: str, **kwargs) -> dict:
    """Galaksi verilerini kurar ve başlangıç durumunu döndürür."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde yok!")
    
    yakit = kwargs.get("yakit", 50)
    
    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }
def yakit_ekle(miktar, depo=None):
  """Varsayılan argüman tuzuğundan kaçınmak için None kalıbı kullanılır."""
  if depo is None:
    depo = []
  depo.append(miktar)
  return depo

