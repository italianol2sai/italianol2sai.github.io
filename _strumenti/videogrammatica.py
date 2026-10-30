"""Link diretti ai video «Videogrammatica in alto!» (cartelle Drive pubbliche di Erila, 2026-10-30), raggruppati per argomento.
I video restano su Drive (scelta di Erila: «con link di drive, chiunque abbia il link»). Uso: python3 _strumenti/videogrammatica.py
→ sostituisce nella home le voci «Videogrammatica A1/A2» con una sottosezione per livello."""
import os, re

D = "https://drive.google.com/file/d/%s/view"
VIDEO = {
 "A1": [
  ("Nomi", [("Nomi regolari", "1zeEaZYUBqrsto55e59Uys3zvTedk23Zd"), ("Nomi irregolari 1: le professioni", "1foTYMfq7AEY0lSnWZngofj7Sypp7BENM"), ("Nomi irregolari 2", "1cVytHJzaCi203SoHi4xzm6-gNNpskbwH")]),
  ("Articoli", [("Gli articoli determinativi", "1dykf49uckm0EerDccvm54MQkdbxG4mc9"), ("Gli articoli indeterminativi", "1DWs_mejBVFjHEAS-RIhamhR4Qt1V5Nbm")]),
  ("Aggettivi, domande, possessivi, dimostrativi", [("Gli aggettivi", "1yvWdLVCqYGz_-JPNnOxJkv1JGrrRrEUz"), ("Gli interrogativi", "11o7c6_Vrm_vJ7TLlvesZntVRr1JxDV0M"),
      ("I possessivi", "1AsUmyR1VhEM-6wpWUJGH2N_unFnohVco"), ("I dimostrativi: aggettivi", "1jMGvto5eoCXyOZveyXgXRaZp3NJ59XR8"), ("I dimostrativi: pronomi", "12dSVq_pjs4idH9JHTlYMeIYqqNs5IiJK")]),
  ("Preposizioni", [("Luogo 1: la provenienza", "1VgE9eMEepBqEea4OnY13xtw35beE_107"), ("Luogo 2: movimento e stato in luogo", "1MK_bLpW5l8VbBHVr3GjCMfKckfv3Dgm6"),
      ("Le preposizioni di tempo", "1fxmLN3VTD3IzH0TYA8ElCgW13_aaPWz3"), ("Con i mezzi di trasporto", "1UXKTZ4pyJrS_JP6e16z97TKCq81QExSz"),
      ("Le preposizioni articolate", "1PJNIEQjp_CupI3qj4PephOlNQRbO_0Mf"), ("Semplice o articolata? 1", "1WsAfmRzPC_eSwNHwJz-ymhOno0hrsf3m"),
      ("A oppure IN?", "1DS73ZpcXxM414VdoQbJwIF2nhER0u_aS"), ("Semplice o articolata? 2", "1xN_CqHcF-TjXEUFBiZrVv5Ou2E65BYSV")]),
  ("Verbi", [("Il presente regolare", "1kIi2aCUNkl7THhv8lc_oyG3IXEHogDdn"), ("I verbi in -care e -gare", "1z7szob8xdB1vEwvvdJJN7SfOHoBZZuiI"),
      ("I verbi riflessivi", "1VZYZk3BN5gAbxGvxVNBayWL3lutKL_Sc"), ("Il presente irregolare 1", "1Z3AamnGPMa-ku-jUiKNV8iwYuizNVU4z"),
      ("Il presente irregolare 2", "1NfKFxNj8ehprOOAc3uyx3ECOQEKCtrTx"), ("Il verbo piacere", "1zBDzomlB46YDu5StLipQiY8oXGMD2N4d"),
      ("Passato prossimo: essere o avere?", "1XsIJCb6Pme5Lth5uTR-X-EpS6xvUBkvV"), ("Passato prossimo: participio regolare", "1pzqLX_Ivr-bF16Y-5-oHINXyS-KkQmof"),
      ("Passato prossimo: participio irregolare", "128NzjiJKsLrV58XMwGnXkupX7x8Nn_0d")]),
  ("Avverbi e indicatori", [("La quantità", "1qt_Y6JvXdluHT49DdJkWeCzPUUEfkmCF"), ("La frequenza", "1Kw_7DBxQH1G0sI9qZFCe0r2Ip1Umg5wf"),
      ("Lo spazio", "1kNsguWz55mvHrkoRTvX9ton10ZCvztAK"), ("Il tempo", "1SBWe2Y8dps3OHvbrIHJpZefbwQQ61MOJ")]),
 ],
 "A2": [
  ("Nomi", [("Plurali irregolari", "140ZolxaIfKOwz77P2uZcEV754mBwGD6M"), ("I nomi alterati", "1DXB1tk2hd4DWvmj_CPnTifnZebldEBP_")]),
  ("Preposizioni", [("Preposizioni di tempo 1", "14djb6nP8c3ZtMfWHoyQzoeqNBJgBH9oT"), ("Preposizioni di tempo 2", "1LOn9QdRK0Ww7g1hOSu3EtCotyp5McTOs"),
      ("Abbigliamento e calzature", "1IDwBGUlAOZRpgE1zlIieCRlNBySrvaSd")]),
  ("Pronomi", [("I pronomi personali", "1O_7Q3MZqQbWeYJTAwkeQQaAj_f5tdaNU"), ("La posizione dei pronomi", "1zFXqa9iglkELevdUOfg54B49LDYIFwEp"),
      ("CE con i pronomi diretti", "1IYi-4GssSjLuOCASmxdG-_AB0Ka7O2p5"), ("Verbi con i pronomi indiretti", "1c73l9iaiWTm_xjz8RCg-f8HAwrITkxsn"),
      ("Altri pronomi", "1t75Z_iHP9qh0Ext9JJnnrM0cXQibrOZO")]),
  ("Aggettivi: buono, bello, comparativi, indefiniti", [("Buono e bello", "16VcU4U56NVkuVcoWlAYEU_Q6u3kriDrZ"), ("I comparativi", "1UMdffiDNhpVKy-oYsB8E6nK2K02-Bbrx"),
      ("I superlativi", "19xy3XgW5hKTHMTSMsIezMLVd-opt_Tzy"), ("Comparativi e superlativi irregolari", "1Pw2A62WmZIqFjlPwUm9VRvwsr1P3nY-1"),
      ("Gli indefiniti 1", "1E10krBmsy2Bcmfgux-rkwog3D4NK5KiC"), ("Gli indefiniti 2", "1LVr4qxnJYDUSPzB4lByuKugbqR_Pf1ac")]),
  ("Avverbi", [("Gli avverbi di modo", "1jrO3MgX9wt4DZ4Tgnb-TBWT2wngZsGGV")]),
  ("Verbi", [("Il passato prossimo", "1r-sxpshfVrLa38dz6ZW0DOsN5uCYy8_V"), ("Verbi riflessivi e reciproci", "1Be9gtN3oF63-rlwDksnNSEZTJCyuFiDH"),
      ("L'imperfetto regolare e irregolare", "1zp7BgkMAgqXUgj0E7ySwMGwTfzjzY0xQ"), ("Quando usiamo l'imperfetto", "1wtITv7naK7Bg8_J_i_r07NWO5otddon7"),
      ("Imperfetto o passato prossimo?", "1N4ubH71CuzQSZFN2F6sNlmsB19_0j0cU"), ("La forma progressiva", "1QxWVIAv2S4d0XtdtEkkkINKPrOP__kWY"),
      ("Il futuro imminente", "1uPn2r2f5WEsqktYyKdGsMCDFWZl8pNXU"), ("Imperativo affermativo: verbi regolari", "1Rg0r1NkK3FFPCNQgl4A53-q1CB8O-H94"),
      ("Imperativo affermativo: verbi irregolari", "1VgHOYQum9ivDiurp5ldjCtQ2dpkGAcL2"), ("Imperativo negativo", "1XWzqPQePIONUTQZ_TZ70e65oeJy62wGM"),
      ("Imperativo con i pronomi", "1Ly4QpYIBmQeMm4x3otd-4jn6Cu25FxD0"), ("Il futuro semplice", "1kvBoLlMRyaBioJD1Wk5T_sbrt_YfoxiI"),
      ("Il futuro semplice irregolare", "1MG4Gzf7ksmAIOe8fm0Xu7G6Va1BpaErB"), ("Il condizionale regolare", "1Z6_JwPZ6_ZR4zK8yWdIClqO-ml_EDej2"),
      ("Il condizionale irregolare", "1Ut0iIo5D_qAEA87urmWGBFBYfnWYSKZB"), ("Le espressioni impersonali", "1O4D2TcKwIU43al9ips8rvPaea1ZwOXjV"),
      ("La forma impersonale", "1QBrc08CmCoIOClBIZOBS1oXUotW6ZyuN")]),
 ],
}

def blocco(lv):
    n = sum(len(v) for _, v in VIDEO[lv])
    righe = []
    for gruppo, video in VIDEO[lv]:
        righe.append('            <p class="nota" style="margin:8px 0 4px"><b>%s</b></p>\n' % gruppo)
        for t, i in video:
            righe.append('            <a class="item ext" href="%s" target="_blank" rel="noopener"><div class="icon">🎬</div>\n'
                         '              <div><strong>%s <span class="tag">%s</span></strong><span>Video su Google Drive</span></div></a>\n' % (D % i, t, lv))
    return ('        <details id="%s-videogrammatica" class="sub">\n          <summary><div class="icon">🎬</div><div><strong>Videogrammatica %s: %d video</strong>'
            '<span>Video brevi di grammatica, divisi per argomento</span></div></summary>\n          <div class="inner">\n%s          </div>\n        </details>\n') % (lv.lower(), lv, n, "".join(righe))

if __name__ == "__main__":
    f = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
    h = open(f, encoding="utf-8").read()
    for lv in VIDEO:
        vecchio = re.compile(r'        <a class="item ext" href="https://drive\.google\.com/drive/folders/[^"]+"[^\n]*\n[^\n]*Videogrammatica %s[^\n]*\n' % lv)
        nuovo_re = re.compile(r'        <details id="%s-videogrammatica" class="sub">.*?\n        </details>\n' % lv.lower(), re.S)
        if nuovo_re.search(h):
            h = nuovo_re.sub(lambda m: blocco(lv), h)
        else:
            assert len(vecchio.findall(h)) == 1, lv
            h = vecchio.sub(lambda m: blocco(lv), h)
    open(f, "w", encoding="utf-8").write(h)
