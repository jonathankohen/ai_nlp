from django.shortcuts import render


def index(req):
    return render(req, "index.html")


def regex(req):
    import re

    if req.method == "POST":
        pattern = r"..."
        incoming_data = req.POST["regexnamefromform"]
        regex_matches = re.findall(pattern, incoming_data)
        return render(req, "regex.html", {"regex_matches": regex_matches})
    else:
        return render(req, "index.html")


def lemma(req):
    import spacy

    nlp = spacy.load("en_core_web_sm")

    if req.method == "POST":
        incoming_data = req.POST["lemmanamefromform"]
        incoming_data = nlp(incoming_data)
        token_list = [i.text for i in incoming_data]
        tokens = [i for i in token_list]
        listof_lemmas = [i.lemma_ for i in incoming_data]
        individual_lemmas = [i for i in listof_lemmas]
        return render(req, "lemma.html", {"tokens": tokens, "individual_lemmas": individual_lemmas})
    else:
        return render(req, "index.html")


def pos(req):
    import spacy

    nlp = spacy.load("en_core_web_sm")

    if req.method == "POST":
        incoming_data = req.POST["posnamefromform"]
        incoming_data = nlp(incoming_data)
        token_list = [i.text for i in incoming_data]
        tokens = [i for i in token_list]
        listof_pos = [i.pos_ for i in incoming_data]
        individual_pos = [i for i in listof_pos]
        listof_explanations = [spacy.explain(i) for i in individual_pos]
        individual_explanations = [i for i in listof_explanations]
        return render(
            req,
            "pos.html",
            {"tokens": tokens, "pos_results": pos_results, "individual_explanations": individual_explanations},
        )
    else:
        return render(req, "index.html")


def ner(req):
    import spacy

    nlp = spacy.load("en_core_web_sm")

    if req.method == "POST":
        incoming_data = req.POST["nernamefromform"]
        incoming_data = nlp(incoming_data)
        token__label_list = [(i.text, i.label_) for i in incoming_data.ents]
        token__labels = [i for i in token__label_list]
        onlylabels = [i.label_ for i in incoming_data.ents]
        listof_explanations = [spacy.explain(i) for i in onlylabels]
        individual_explanations = [i for i in listof_explanations]

        return render(
            req,
            "ner.html",
            {"token__labels": token__labels, "individual_explanations": individual_explanations},
        )
    else:
        return render(req, "index.html")
