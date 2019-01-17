from lxml import etree
import requests
from io import StringIO
import sys
import svgwrite
from svgwrite import cm, mm


# Recuperation du fichier par un flux HTTP
def chargerFlux(url):
    # creation d'une reponse de la requete a partir du lien
    resp = requests.get(url)

    content = resp.content;
    # sauvegarde du fichier XML
    with open('myxml2.xml', 'wb') as f:
        f.write(content)

    return content

# Conversion du fichier XML en fichier SVG
def svg_conversion(name, entity, relation, attribute):
    # contenant des elements SVG
    dwg = svgwrite.Drawing(filename=name, debug=True, size=("900px", "650px"))

    # ----------------------------------------------------------------------------------
    # Representation des entites
    # Entite 1
    dwg.add(dwg.rect(insert=(2*cm, 2*cm), size=(45*mm, 45*mm),
                       fill='white', stroke='red', stroke_width=3))

    # Entite 2
    dwg.add(dwg.rect(insert=(18*cm, 2*cm), size=(45*mm, 45*mm),
                       fill='white', stroke='red', stroke_width=3))

    # Entite 3
    dwg.add(dwg.rect(insert=(18*cm, 12*cm), size=(45*mm, 45*mm),
                       fill='white', stroke='red', stroke_width=3))

    # ---------------------------------------------------------------------------------
    # Representation des noms des entites
    # Nom de l'entite 1
    dwg.add(dwg.text(entity[0],
                     insert=(3*cm, 3*cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )
    # Nom de l'entite 2
    dwg.add(dwg.text(entity[1],
                     insert=(19*cm, 3*cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )
    # Nom de l'entite 3
    dwg.add(dwg.text(entity[2],
                     insert=(19*cm, 13*cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )

    # ----------------------------------------------------------------------------
    # Ajout du trait du rectangle
    # ligne pour Entite 1
    dwg.add(dwg.line(start=(2 * cm, 3.5 * cm),
                        end=(6.5 * cm, 3.5 * cm),
                        stroke='red',
                        stroke_width=3)
               )
    # ligne pour Entite 2
    dwg.add(dwg.line(start=(18 * cm, 3.5 * cm),
                        end=(22.5 * cm, 3.5 * cm),
                        stroke='red',
                        stroke_width=3)
               )
    # ligne pour Entite 3
    dwg.add(dwg.line(start=(18 * cm, 13.5 * cm),
                        end=(22.5 * cm, 13.5 * cm),
                        stroke='red',
                        stroke_width=3)
               )

    # -------------------------------------------------------------------------
    # Representation des associations
    # ligne horizontale
    dwg.add(dwg.line(start=(6.5 * cm, 4 * cm),
                        end=(18 * cm, 4 * cm),
                        stroke='red',
                        stroke_width=3)
               )
    # ligne verticale
    dwg.add(dwg.line(start=(20 * cm, 6.5 * cm),
                        end=(20 * cm, 12 * cm),
                        stroke='red',
                        stroke_width=3)
               )

    # -----------------------------------------------------------------------------
    # Representation des ellipses
    dwg.add(dwg.ellipse(center=(12*cm, 4*cm),
                           r=('3cm', '8mm'),
                           fill='white',
                           stroke='red')
               )

    dwg.add(dwg.ellipse(center=(20 * cm, 9 * cm),
                           r=('3cm', '8mm'),
                           fill='white',
                           stroke='red')
               )

    # ----------------------------------------------------------------------------
    # Representation des attributs
    # Les attributs de l'entite 1
    dwg.add(dwg.text(attribute[0],
                     insert=(3 * cm, 4 * cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )
    # Les attributs de l'entite 2
    dwg.add(dwg.text(attribute[1],
                     insert=(19 * cm, 4 * cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )
    # Les attributs de l'entite 3
    dwg.add(dwg.text(attribute[2],
                     insert=(19 * cm, 14 * cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )

    # --------------------------------------------------------------------
    # Respresentation des noms des asscociations
    # Nom de la relation 1
    dwg.add(dwg.text(relation[0],
                     insert=(11 * cm, 4.2 * cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )
    # Nom de la relation 2
    dwg.add(dwg.text(relation[1],
                     insert=(19 * cm, 9.2 * cm),
                     stroke='none',
                     fill=svgwrite.rgb(15, 15, 15, '%'),
                     font_size='18px',
                     font_weight="bold")
            )
    # souvegarde du fichier svg
    dwg.save()


if __name__ == '__main__':

    # -----------------------------------------------------------------------------
    # Validation et extraction du fichier XML

    filename_xml = sys.argv[1]

    # ouverture et lecture du fichier XML
    with open(filename_xml, 'r') as xml_file:
        xml_to_check = xml_file.read()

    # parsing du fichier xml
    try:
        doc = etree.parse(StringIO(xml_to_check))
        print('Le document XML est bien formé !')

    # recherche de l'erreur dans le fichier
    except IOError:
        print("Le document XML n'est pas bien formé !")

    # Extraction des entites, associations, et des attributs

    # lecture du fichier dans le disque et creation d'un objet arbre
    tree = etree.parse(filename_xml)
    '''root = tree.getroot()
    root_tag = root.tag
    print(root_tag)'''

    entities = []
    associations = []
    attributes = []
    i = 0

    print("Les entités :")
    for entity in tree.xpath("/EABooks/entity"):
        entities.append(entity.get("Name"))
        i += 1
        print(entity.get("Name"))
        print("-----------------------------------")

    print("Les associations :")
    for association in tree.xpath("/EABooks/association"):
        e1 = association.get("entity1")
        e2 = association.get("entity2")
        associations.append(association.text)
        i += 1
        print(e1, "----", association.text, "--->", e2)
        print("-----------------------------------")

    print("Les attributs des entités :")
    for attribute in tree.xpath("/EABooks/entity/attribute"):
        attributes.append(attribute.get("Name"))
        i += 1
        print(attribute.get("entity"), ":", attribute.get("Name"))
        print("-----------------------------------")

    # -------------------------------------------------------------------------
    # Conversion du fichier en SVG

    svg_conversion('ea.svg', entities, associations, attributes)







