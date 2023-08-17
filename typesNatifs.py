# Les types natifs
# Les chaînes de caractères { str() }
# Liste exhaustive des caractères spéciaux interpreter par python
# {
#     "\a" => "caractère d'appel (BEL)",
#     "\b" => "caractère de retour arrière",
#     "\f" => "saut de page",
#     "\n" => "retour à la ligne",
#     "\r" => "retour chariot",
#     "\t" => "tabulation horizontal",
#     "\v" => "tabulation verticale"
# }
print("Hello Wolrd!")
print('Je m\'appelle Lybe_')
print("""Je suis une chaîne de caractères
      comme les autres, mais je m'étends
      sur plusieurs lignes.""")
print("a\nb")
print("\u2764")
print('c:\dossiers\thibault\nouveautes')
print(r'c:\dossiers\thibault\nouveautes')

# Les nombres
# Les nombres entiers { int() }
print(-5)
print(1)
print(250)
print(135843125498711354154815)
print(1000000)
print(1_000_000)

# Les nombres décimaux (flottants) { float() }
print(-5.485)
print(1.254)
print(150.87)
print(10.0)

# Les booléens { bool() }
# 1 = true
# 0 = false
# "" = false
# 0.0 = false
# [] = false
# {} = false
issubclass(bool, int)
bool("bonjour")

# Les types séquentiels (listes, tuples)
# Les types d'ensembles (set, frozenset)
# Les types de correspondances (dictionnaire)
