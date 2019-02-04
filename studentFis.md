---
title: Budi student FIŠ-a
description: >
  Prezentacija prikazuje zašto uspešno izvršavamo obaveze svih 10 godina !
hide_description: true
menu: true
order: 2
permalink: /budi-student-fis-a/
comments: true

---

- Prezentacija prikazuje zašto uspešno izvršavamo obaveze svih 10 godina !
	- [Budi student FIŠ-a](/courses/fis/fis.html){:target="_blank"} --- PC & Mobile view.
  {:.faded}

  - Sva pitanja možete napisati na kraju stranice u obliku komentara


	
## Konkurs (zahtev za đake iz Srbije)

- Ukoliko ste odlučili da studirate na FIŠ-u pratite sledeće korakte:
	- Ispunite formu u nastavku
	- Pre klika na **POŠALJI** proverite još jednom podatke
	- Za **najkasnije 5 radnih dana** će te dobiti odgovor na Vaš zahtev


<form action="//formspree.io/{{ site.author.email }}?Subject=Zahtev%20za%20upis%20na%20FIŠ"
      method="POST">
    <input type="hidden" name="FIS" value="Zahtev za upis na FIS" />
    <label for="exampleInputEmail1">Ime i prezime</label>
  <input type="text" name="ImePrezime" class="form-control" placeholder="Unesite ime i prezime" required>
  <label for="exampleInputEmail1">Grad/Mesto</label>
  <input type="text" name="Grad" class="form-control" placeholder="Unesite odakle ste" required>
  <label for="exampleInputEmail1">Godine</label>
    <div class="form-row">
      <div class="col-6">
        <input type="number" name="Godine" class="form-control" placeholder="Unesite godine" required>
      </div>
  </div>
    <label for="exampleInputEmail1">Naziv i mesto škole</label>
  <input type="text" name="Skola" class="form-control" placeholder="Unesite naziv skole" required>
    <input type="text" name="Mesto" class="form-control" placeholder="Unesite mesto" required>
    <label for="exampleInputEmail1">Prosek za svaku godinu</label>
  <div class="form-row">
      <div class="col-5">
        <input type="text" name="1Godina" class="form-control" placeholder="I godina" required>
      </div>
      <div class="col-5">
          <input type="text" name="2Godina" class="form-control" placeholder="II godina" required>
      </div>
      <div class="col-5">
        <input type="text" name="3Godina" class="form-control" placeholder="III godina" required>
      </div>
      <div class="col-5">
          <input type="text" name="4Godina" class="form-control" placeholder="IV godina" required>
      </div>
  </div>
    <label for="exampleInputEmail1">Kontakt</label>
        <input type="email" name="Mail" class="form-control"  placeholder="mejl@primer.com" required>
          <input type="text" name="Telefon" class="form-control" placeholder="Unesite broj telefona +381" required>
  <div class="col-8">
      <label for="exampleFormControlSelect1">Potvrda za upisom </label>
      <select class="form-control" type="text" name="Potvrda" id="exampleFormControlSelect1">
        <option>Mala</option>
        <option>Jos uvek razmisljam</option>
        <option>Nije sigurno</option>
        <option>Velika</option>
        <option>Sigurno dolazim</option>
      </select>
    </div>
      <div class="form-group">
    <label for="exampleFormControlTextarea1">Motivaciono pismo</label>
    <textarea class="form-control" type="text" name="MotivacionoPismo"  rows="7" placeholder="Napišite Vašu motivaciju za studiranje na FIŠ-u" required></textarea>
  </div>
    <input type="hidden" name="_next" value="{{ site.baseurl }}/zahtev-poslat" />
    <input type="hidden" name="_subject" value="New submission from {{ site.url }}{{ site.baseurl }}" />
    <input type="text" name="_gotcha" style="display:none" />
    <button type="submit" class="btn btn-primary">Pošalji</button>
    <button type="reset" class="btn btn-primary">Resetuj</button>
</form>

