from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "tajny_klic_pro_session"  # Tajný klíč pro použití session

# Data pro jednotlivé pojmy
concepts = {
    "počítač": "Počítač je stroj, který zpracovává informace pomocí hardwaru a softwaru.",
    "paměť počítače": "Paměť počítače je hardware, který slouží k ukládání dat a instrukcí, které počítač potřebuje pro svůj běh. Existují různé typy pamětí, jako je RAM (operační paměť), ROM (paměť pouze pro čtení), a cache paměť.",
    "adresa paměti": "Adresa paměti je jednoznačný identifikátor pro konkrétní místo v paměti počítače, kde jsou uložena data nebo instrukce.",
    "operační systém": "Operační systém poskytuje základní funkce a prostředí pro běh aplikací.",
    "adresář": "Adresář (složka) slouží k organizaci souborů a dalších adresářů.",
    "soubor": "Soubor obsahuje data, která mohou být text, obrázky, kód nebo cokoli jiného.",
    "virtuální prostředí": "Virtuální prostředí izoluje závislosti vašeho projektu od globálního prostředí.",
    "instalace": "Instalace do virtuálního prostředí přidává knihovny a nástroje, které váš projekt potřebuje.",
    "závislosti": "Závislosti jsou knihovny a nástroje, které váš projekt potřebuje k fungování.",
    "app.py": "app.py je hlavní soubor vaší aplikace, který obsahuje kód pro vytvoření webové stránky.",
    "adresa": "http://127.0.0.1:5000 je adresa, na které běží váš Flask server."
}

# Definice obousměrných vztahů mezi pojmy
concept_relations = {
    "počítač": ["paměť počítače", "operační systém"],
    "paměť počítače": ["počítač", "adresa paměti"],  # Přidán zpětný odkaz na "počítač"
    "adresa paměti": ["paměť počítače"],  # Přidán zpětný odkaz na "paměť počítače"
    "operační systém": ["počítač", "adresář", "soubor"],  # Přidán zpětný odkaz na "počítač"
    "adresář": ["operační systém", "soubor"],  # Přidán zpětný odkaz na "operační systém"
    "soubor": ["operační systém", "adresář"],  # Přidán zpětný odkaz na "operační systém" a "adresář"
    "virtuální prostředí": ["instalace", "závislosti"],
    "instalace": ["virtuální prostředí", "závislosti"],  # Přidán zpětný odkaz na "virtuální prostředí"
    "závislosti": ["virtuální prostředí", "instalace"],  # Přidán zpětný odkaz na "virtuální prostředí" a "instalaci"
    "app.py": [],  # Tento pojem nemá další odkazy
    "adresa": [],  # Tento pojem nemá další odkazy
}

@app.route("/")
def index():
    # Inicializace session, pokud neexistuje
    if "explored" not in session:
        session["explored"] = []
    return render_template("index.html", explored=session["explored"], concepts=concepts)

    
@app.route("/snowflake/<concept>")
def snowflake(concept):
    if "explored" not in session:
        session["explored"] = []

    if concept not in session["explored"]:
        session["explored"].append(concept)
        session.modified = True  # Uložení změn v session

    description = concepts.get(concept, "Pojem nebyl nalezen.")
    return render_template(
        "snowflake.html",
        concept=concept,
        description=description,
        explored=session["explored"],  # Předání explored do šablony
        concept_relations=concept_relations  # Předání concept_relations do šablony
    )

@app.route("/christmas")
def christmas():
    return render_template("christmas.html")
    
@app.route("/map")
def map():
    return render_template("map.html", concept_relations=concept_relations, concepts=concepts)

@app.route("/reset")
def reset():
    # Resetování session
    session["explored"] = []
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
