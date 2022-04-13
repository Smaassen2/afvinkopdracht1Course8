from flask import Flask, render_template, request
import mysql.connector
#constructor
app = Flask(__name__)

#url


@app.route('/', methods=["POST", "GET"])
def biosearch():
    if request.method == "POST":
        zoekterm = request.form.get("zoekterm", "")
        # connect aan de database
        conn = mysql.connector.connect(host="ensembldb.ensembl.org", user="anonymous", db="homo_sapiens_core_95_38")
        # open een cursor
        cursor = conn.cursor()

        # voer een query uit
        cursor.execute("select description from gene where description like '%" + zoekterm + "%'")


        # haal de rijen op
        alle_rijen = cursor.fetchall()
        desc_met_zoekterm = []
        for desc in alle_rijen:
            desc_met_zoekterm.append(desc[0])
        # sluiten van cursor en connectie
        print("test")
        cursor.close()
        conn.close()
        return render_template("opdracht.html", zoekterm=zoekterm, result=desc_met_zoekterm,
                               len_results=len(desc_met_zoekterm))
    else:
        return render_template("opdracht.html", zoekterm="", result="", len_results=0)

if __name__ == '__main__':
    app.run()