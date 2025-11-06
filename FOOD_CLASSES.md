# 🍕 Food-101 Classes - Ce poate recunoaște modelul

## ✅ Ce POATE recunoaște
Modelul Food-101 este antrenat pe **101 clase de mâncăruri PREPARATE**. Funcționează cel mai bine cu:
- Pizza, burgeri, hot dogs
- Paste (spaghetti, lasagna, ravioli)
- Deserturi (cheesecake, tiramisu, donuts)
- Salate (caesar salad, greek salad)
- Mâncăruri asiatice (sushi, ramen, pad thai)
- Etc. (vezi lista completă mai jos)

## ❌ Ce NU poate recunoaște
- **Ingrediente crude** (mere, roșii, cartofi cruzi, ceapă, etc.)
- **Fructe simple** (banane, portocale, struguri, etc.)
- **Legume simple** (ardei, castraveți, morcovi, etc.)
- **Mâncăruri care NU sunt în listă** (shawarma, kebab, cozonac, etc.)

## 🎯 Cum funcționează
Când încrederea modelului este < 50%, returnează **"Unknown"** pentru că:
1. Imaginea NU conține o mâncare din Food-101
2. Unghiul/lighting-ul e prost
3. E un ingredient crud, nu o mâncare preparată

## 📋 Lista COMPLETĂ a celor 101 clase

1. apple_pie
2. baby_back_ribs
3. baklava
4. beef_carpaccio
5. beef_tartare
6. beet_salad
7. beignets
8. bibimbap
9. bread_pudding
10. breakfast_burrito
11. bruschetta
12. caesar_salad
13. cannoli
14. caprese_salad
15. carrot_cake
16. ceviche
17. cheese_plate
18. cheesecake
19. chicken_curry
20. chicken_quesadilla
21. chicken_wings
22. chocolate_cake
23. chocolate_mousse
24. churros
25. clam_chowder
26. club_sandwich
27. crab_cakes
28. creme_brulee
29. croque_madame
30. cup_cakes
31. deviled_eggs
32. donuts
33. dumplings
34. edamame
35. eggs_benedict
36. escargots
37. falafel
38. filet_mignon
39. fish_and_chips
40. foie_gras
41. french_fries
42. french_onion_soup
43. french_toast
44. fried_calamari
45. fried_rice
46. frozen_yogurt
47. garlic_bread
48. gnocchi
49. greek_salad
50. grilled_cheese_sandwich
51. grilled_salmon
52. guacamole
53. gyoza
54. hamburger
55. hot_and_sour_soup
56. hot_dog
57. huevos_rancheros
58. hummus
59. ice_cream
60. lasagna
61. lobster_bisque
62. lobster_roll_sandwich
63. macaroni_and_cheese
64. macarons
65. miso_soup
66. mussels
67. nachos
68. omelette
69. onion_rings
70. oysters
71. pad_thai
72. paella
73. pancakes
74. panna_cotta
75. peking_duck
76. pho
77. pizza
78. pork_chop
79. poutine
80. prime_rib
81. pulled_pork_sandwich
82. ramen
83. ravioli
84. red_velvet_cake
85. risotto
86. samosa
87. sashimi
88. scallops
89. seaweed_salad
90. shrimp_and_grits
91. spaghetti_bolognese
92. spaghetti_carbonara
93. spring_rolls
94. steak
95. strawberry_shortcake
96. sushi
97. tacos
98. takoyaki
99. tiramisu
100. tuna_tartare
101. waffles

---

## 💡 Pentru viitor: Cum să extindem modelul

Dacă vrei să recunoști și ingrediente crude (mere, banane, etc.), ai nevoie de:

### Opțiunea 1: Model combinat
- Folosește **2 modele**: unul pentru Food-101, altul pentru ingrediente (ex: ImageNet)
- Backend verifică ambele și returnează cel mai bun rezultat

### Opțiunea 2: Fine-tuning custom
- Antrenezi propriul model pe un dataset extins
- Combină Food-101 + imagini de ingrediente
- Necesită mult timp și resurse (GPU)

### Opțiunea 3: Folosește un model mai general
- **Google Vision API** - recunoaște aproape orice
- **CLIP** de la OpenAI - foarte versatil
- Costă bani sau necesită mai multă memorie
