# Tuntiharjoitus 1–3: Tuotteiden hallinta (Flask + SQLite)

Tämä repositorio sisältää Web-ohjelmointi ja sovelluskehykset 2025 -kurssin tehtävät 1–3.  
Tehtävissä toteutetaan tuotteiden haku -järjestelmä käyttäen MVC-, Repository-, Factory- ja Service-suunnittelumalleja.

---

## Projektin rakenne

```
tuntiharjoitus1_3_products/
├── app.py
├── models/
│   └── models.py
├── controllers/
│   └── products_controller.py
├── repositories/
│   └── products_repository.py
├── services/
│   └── products_service.py
├── factories/
│   └── products_factory.py
├── decorators/
│   └── products_service.py
└── products.db
```

---

## Tehtävä 1: MVC-rakenne

- Toteutettiin `Tuote`-malli  
- Lisättiin `/api/products` ja `/api/products/<id>` -reitit  
- Tehtiin `products_controller.py`  
- Flask-sovellus toimii perustason MVC-mallin mukaan  

---

## Tehtävä 2: Repository- ja Factory-suunnittelumallit

- Lisättiin `ProductsRepository`  
- Repository vastaa tietokantakyselyistä (SQLite)  
- Toteutettiin `products_factory.py`  
- Lisättiin `decorators/products_service.py` riippuvuuksien injektointiin  
- Controller ei enää käsittele tietokantaa suoraan  

---

## Tehtävä 3: Service-suunnittelumalli

- Lisättiin `ProductsService`  
- Palvelukerros sisältää sovelluslogiikan  
- Controller käyttää vain serviceä  
- Repository injektoidaan servicen kautta  

---

## Käynnistys

Asenna riippuvuudet:

```
pip install -r requirements.txt
```

Käynnistä sovellus:

```
python app.py
```

---

## API-endpointit

### Hae kaikki tuotteet
```
GET /api/products
```

### Hae tuote ID:n perusteella
```
GET /api/products/<id>
```

---

## Teknologiat

- Python 3  
- Flask  
- SQLite  
- MVC  
- Repository Pattern  
- Factory Pattern  
- Service Layer Pattern  
- Dependency Injection (decorator)  

---

## Kurssi
**Web-ohjelmointi ja sovelluskehykset 2025**
