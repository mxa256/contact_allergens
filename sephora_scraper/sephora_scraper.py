#We will need to scrape the sephora website at some point
#For now (proof of concept) we will generate a small dataset of products

import pandas as pd

#Make a dictionary of products
data = [
    {
        "Product Name": "Summer Fridays",
        "Brand": "Lip Butter Balm for Hydration & Shine",
        "Ingredients": "Phytosteryl/Isostearyl/Cetyl/Stearyl/Behenyl Dimer Dilinoleate, Diisostearyl Malate, Hydrogenated Polyisobutene, Polybutene, Hydrogenated Poly (C6-14 Olefin), Butyrospermum Parkii (Shea) Butter, Microcrystalline Wax/Cera Microcristallina/Cire Microcristalline, Octyldodecanol, Synthetic Wax, Disteardimonium Hectorite, Astrocaryum Murumuru Seed Butter, Sodium Hyaluronate, Vanillin, Tocopherol, Propylene Carbonate, Polyglyceryl-2 Diisostearate, Mica, BHT"
    },
    {
        "Product Name": "Dr. Jart+",
        "Brand": "Premium BB Tinted Moisturizer with Niacinamide and SPF 40",
        "Ingredients": "WATER/AQUA/EAU, CYCLOPENTASILOXANE, CYCLOHEXASILOXANE, GLYCERIN, PEG-10 DIMETHICONE, TALC, HEXYL LAURATE, DIPROPYLENE GLYCOL, C12-15 ALKYL BENZOATE, NIACINAMIDE, DIPHENYLSILOXY PHENYL TRIMETHICONE, DISTEARDIMONIUM HECTORITE, CITRUS AURANTIUM BERGAMIA (BERGAMOT) FRUIT OIL, CITRUS LIMON (LEMON) PEEL OIL, CITRUS AURANTIFOLIA (LIME) OIL, PINUS SYLVESTRIS (PINE) LEAF OIL, CITRUS AURANTIUM DULCIS (ORANGE) PEEL OIL, ADENOSINE, ALLANTOIN, ETHYLHEXYLGLYCERIN, TRIHYDROXYSTEARIN, POLYGLYCERYL-6 POLYRICINOLEATE, METHICONE, DIMETHICONE,DIMETHICONE/VINYL DIMETHICONE CROSSPOLYMER, 1,2-HEXANEDIOL, TRIETHOXYCAPRYLYLSILANE, MAGNESIUM SULFATE, EUCALYPTUS GLOBULUS LEAF OIL, LIMONENE, TOCOPHEROL, BHT, PHENOXYETHANOL, TITANIUM DIOXIDE (CI 77891), IRON OXIDES (CI 77492), IRON OXIDES (CI 77491), IRON OXIDES (CI 77499)"
    },
    {
        "Product Name": "Zari Eyes Long-Lasting Crease-Proof Cream Eyeshadow",
        "Brand": "Kulfi",
        "Ingredients": "Isododecane, Mica, Silica, Trimethylsiloxysilicate, Disteardimonium Hectorite, Tribehenin, Bis-Diglyceryl Polyacyladipate-2, Synthetic Beeswax, Propylene Carbonate, Stearalkonium Hectorite, Tocopherol, Tocopheryl Acetate, Aloe Barbadensis Leaf Juice Powder*, Phyllanthus Emblica Fruit Extract, Anthemis Nobilis Flower Extract, Glycerin, Jojoba Esters, Isopropyl Jojobate, Jojoba Alcohol, Tin Oxide, Maltodextrin, Water (Aqua) (Eau), Phenoxyethanol, Ethylhexylglycerin, Titanium Dioxide (CI 77891), Ferric Ferrocyanide (CI 77510)"
    },
    {
        "Product Name": "Drunk Elephant",
        "Brand": "T.L.C. Sukari Babyfacial™ AHA + BHA Mask",
        "Ingredients": "Water, Glycolic Acid, Hydroxyethyl Acrylate/Sodium Acryloyldimethyl Taurate Copolymer, Glycerin, Sodium Hydroxide, Salicylic Acid, Aloe Barbadensis Leaf Extract, Camellia Oleifera Leaf Extract, Lactobacillus/Pumpkin Ferment Extract, Lactobacillus/Punica Granatum Fruit Ferment Extract, Opuntia Ficus-Indica Extract, Pyrus Malus (Apple) Fruit Extract, Silybum Marianum Seed Extract, Saccharomyces Cerevisiae Extract, Vitis Vinifera (Grape) Juice Extract, Camellia Sinensis Leaf Powder, Cicer Arietinum Seed Powder, Sclerocarya Birrea Seed Oil, Passiflora Edulis Seed Oil, Leuconostoc/Radish Root Ferment Filtrate, Sodium Hyaluronate Crosspolymer, Sodium PCA, Allantoin, Dipotassium Glycyrrhizate, Dextrin, Polydextrose, Sorbitan Isostearate, Amylopectin, Niacinamide, Phytosphingosine, Lactic Acid, Propanediol, Citric Acid, Titanium Dioxide, Trisodium Ethylenediamine Disuccinate, Polysorbate 60, Caprylyl Glycol, Chlorphenesin, Phenoxyethanol"
    },
    {
        "Product Name": "Kiehl's Since 1851",
        "Brand": "Ultra Facial Refillable Moisturizing Cream with Squalane",
        "Ingredients": "Aqua / Water , Glycerin , Dimethicone , Squalane , Bis-Peg-18 Methyl Ether Dimethyl Silane , Sucrose Stearate , Stearyl Alcohol , Peg-8 Stearate , Myristyl Myristate , Prunus Armeniaca Kernel Oil / Apricot Kernel Oil , Phenoxyethanol , Persea Gratissima Oil / Avocado Oil , Glyceryl Stearate , Cetyl Alcohol , Oryza Sativa Bran Oil / Rice Bran Oil , Olea Europaea Fruit Oil / Olive Fruit Oil , Chlorphenesin , Stearic Acid , Palmitic Acid , Carbomer , Acrylates/C10-30 Alkyl Acrylate Crosspolymer , Trisodium Ethylenediamine Disuccinate , Prunus Amygdalus Dulcis Oil / Sweet Almond Oil , Xanthan Gum , Ethylhexylglycerin , Sodium Hydroxide , Tocopherol , Glycine Soja Oil / Soybean Oil , Pseudoalteromonas Ferment Extract , Myristic Acid , Hydroxypalmitoyl Sphinganine , Salicylic Acid , Helianthus Annuus Seed Oil / Sunflower Seed Oil , Rosmarinus Officinalis Leaf Extract / Rosemary Leaf Extract , Citric Acid"
    },
    {
        "Product Name": "Tower 28 Beauty",
        "Brand": "MakeWaves Lengthening + Volumizing Mascara",
        "Ingredients": "Water/Aqua/Eau, Copernicia Cerifera (Carnauba) Wax/Cera Carnauba/Cire de carnauba, Glyceryl Stearate, Hydrogenated Olive Oil Stearyl Esters, Synthetic Wax, VP/VA Copolymer, Stearic Acid, Helianthus Annuus (Sunflower) Seed Wax, Palmitic Acid, Butylene Glycol, Olea Europaea (Olive) Oil Unsaponifiables, Aminomethyl Propanol, Ricinus Communis (Castor) Seed Oil, 1,2-Hexanediol, Caprylyl Glycol, Polyimide-1, Galactoarabinan, Rhus Succedanea Fruit Wax, Shorea Robusta Resin, Sodium Dehydroacetate, Lecithin, Tocopherol, Ascorbyl Palmitate, Citric Acid, Iron Oxides (CI 77499), Ultramarines (CI 77007)"
    },
    {
        "Product Name": "Sol de Janeiro",
        "Brand": "Cheirosa 62 Bum Bum Hair & Body Perfume Mist",
        "Ingredients": "Alcohol Denat., Aqua (Water, Eau), Parfum (Fragrance), Benzyl Alcohol, Benzyl Salicylate, Hydroxycitronellal, Coumarin, Limonene, Linalool, Benzyl Benzoate, Citral, Eugenol"
    },
    {
        "Product Name": "NARS",
        "Brand": "Soft Matte Complete Full Coverage Longwear Concealer",
        "Ingredients": "orthesin, Dimethicone, Water, Glycerin, Butylene Glycol, Nylon-12, Paraffin, Dimethicone/Vinyl Dimethicone Crosspolymer, Dicaprylyl Carbonate, Zinc Oxide, Peg-10 Dimethicone, Peg-400, Sorbitan Sesquiisostearate, Microcrystalline Wax/Cera Microcristallina, Aluminum Hydroxide, Phenoxyethanol, Polysilicone-2, Silica, Barium Sulfate, Dextrin Palmitate, Distearyldimonium Chloride, Palmitic Acid, Hydrogen Dimethicone, Palmitoyl Tripeptide-5, Ascorbic Acid, Retinyl Palmitate, Tocopheryl Acetate, Alumina, Sodium Acetylated Hyaluronate, Tocopherol, [+/- (May Contain): Mica, Titanium Dioxide (Ci 77891), Iron Oxides (Ci 77491), Iron Oxides (Ci 77492), Iron Oxides (Ci 77499)]"
    },
    {
        "Product Name": "Patrick Ta",
        "Brand": "Major Skin Hydra-Luxe Luminous Skin Perfecting Foundation For Natural Glow",
        "Ingredients": "Cananga Oil, Water (Aqua, Eau), Glycerin, Isononyl Isononanoate, Propanediol, Dicaprylyl Ether, Squalane, Pentaerythrityl Tetraisostearate, Hydrogenated Styrene/Methylstyrene/Indene Copolymer, Hydrogenated Ethylhexyl Olivate, Polyglyceryl-6 Polyricinoleate, Polyglyceryl-2 Dipolyhydroxystearate, Isostearyl Neopentanoate, C9-12 Alkane, Dimer Dilinoleyl Dimer Dilinoleate, Polyglyceryl-2 Isostearate, PVP, Lauroyl Lysine, Dipalmitoyl Hydroxyproline, Myristyl Myristate, Magnesium Sulfate, Disteardimonium Hectorite, Lecithin, Phenoxyethanol, Propylene Carbonate, Zinc Stearate, Octyldodecyl Stearoyl Stearate, Hydrogenated Lecithin, Butyrospermum Parkii (Shea) Butter, Sodium Benzoate, Saccharomyces/Xylinum/Black Tea Ferment, Distarch Phosphate, Allantoin, Hydrogenated Olive Oil Unsaponifiables, Coco-Caprylate/Caprate, Tocopherol, Sodium Hyaluronate, Sodium Dehydroacetate, Helianthus Annuus (Sunflower) Seed Oil, Pentaerythrityl Tetra-di-t-butyl Hydroxyhydrocinnamate, Potassium Sorbate, May Contain (+/-): Titanium Dioxide (CI 77891), Iron Oxides (CI 77491, CI 77492, CI 77499)"
    } #Added canaga oil for proof of concept
]

#Convert to DataFrame
df = pd.DataFrame(data)

#Save to csv
df.to_csv("products_small_batch.csv", index=False)

print(df)
