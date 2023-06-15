# --- variables need to run GA ---
base_df = None  # to be updated by user input from GUI
GRID_R = 198
GRID_C = 196

TEMP_PER_AG = 0.0038
TEMP_PER_CON = -0.0020
TEMP_PER_URB = 0.0103
TEMP_PER_WATER = 0
TEMP_PER_HERB = 0.0072
TEMP_TARGET = 2

PPL_PER_URB = 514
PPL_CURRENT = 4157733
PPL_GROWTH = 1000000

LU_INSUFFICIENT = (3,)
LU_EXCESS = (5,)

min_conf = 0
max_conf = GRID_C * GRID_R

# --- Column names for the input DataFrame ---
AG_SUIT = "ag_suit"  # agriculture suitability
CON_SUIT = "con_suit"  # conservation suitability
URB_SUIT = "urb_suit"  # urban suitability
CURRENT_LU = "current_lu"  # current land use

# --- GA parameters ---
CXPB = 0.6  # crossover probability
MUTPB = 0.5  # mutation probability
GEN_NUM = 100  # number of generations
POP_SIZE = 100  # population size

# --- Initial sampling probability for each land use ---
INIT_PROB_AG = {1: 0.1, 2: 0.2, 3: 0.7}
INIT_PROB_CON = {1: 0.1, 2: 0.1, 3: 0.8}
INIT_PROB_URB = {1: 0.1, 2: 0.3, 3: 0.6}
INIT_SAMPLE_SIZE = 3000  # number of cells changing its land use

test = ["N/A"]
ahafo = [
    "Entire Region",
    "Asuogyaman",
    "Asutifi North",
    "Atebubu Amantin",
    "Atiwa East",
    "Tempane",
    "Tolon",
]

ashanti = [
    "Entire Region",
    "Adansi North",
    "Adansi South",
    "Adentan",
    "Afigya Kwabre South",
    "Agona East",
    "Ahafo Ano South East",
    "Ahafo Ano South West",
    "Ahanta West",
    "Akwapim North",
    "Amansie South",
    "Amansie West",
    "Anloga",
    "Asante Akim South",
    "Asene Manso Akroso",
    "Ashaiman",
    "Assin Fosu",
    "Assin North",
    "Atwima Nwabiagya North",
    "Atwima Nwabiagya South",
    "Awutu Senya",
    "Awutu Senya East",
    "Berekum West",
    "Builsa North",
    "Builsa South",
    "Ekumfi",
    "Ellembelle",
    "Karaga (Karaga)",
    "Kwaebibirem",
    "Kwahu Afram Plains South",
    "Kwahu East",
    "Mpohor",
    "Okaikoi North",
    "Okere",
    "Old Tafo",
    "Prestea/Huni Valley",
    "Pru East",
    "Saboba",
    "Sene West",
    "Shai Osudoku",
    "Shama",
    "Sissala East",
    "Sissala West",
    "Tano North",
]

bono = [
    "Entire Region",
    "Bawku West",
    "Bia East",
    "Bia West",
    "Dormaa West (Nkran Nkwanta)",
    "East Gonja",
    "East Mamprusi",
    "Jasikan",
    "Jomoro",
    "Tarkwa-Nsuaem",
    "Tatale Sanguli",
    "Techiman",
]

bono_east = [
    "Entire Region",
    "Atiwa West",
    "Korle Klottey",
    "Kpandai",
    "North Dayi",
    "North East Gonja",
    "Savelugu",
    "Sawla Tuna Kalba",
    "South Dayi",
    "South Tongu",
    "Upper Denkyira East",
    "Upper Denkyira West",
]

central = [
    "Entire Region",
    "Abura Asebu Kwamankese",
    "Agona West",
    "Agortime-Ziope",
    "Akatsi North",
    "Asokwa",
    "Assin South",
    "Asunafo North",
    "Asunafo South",
    "Ayawaso Central",
    "Ayawaso East",
    "Central Tongu",
    "Ejura Sekyedumase",
    "Fanteakwa North",
    "Gomoa West",
    "Gushegu",
    "Ho",
    "Kpando",
    "Nadowli Kaleo",
    "Wa West",
    "Wassa Amenfi East",
    "Wassa Amenfi West",
    "Wassa East",
]

eastern = [
    "Entire Region",
    "Abuakwa North",
    "Abuakwa South",
    "Ada East",
    "Akwapim South",
    "Akyemansa",
    "Amansie Central",
    "Asikuma Odoben Brakwa",
    "Asutifi South",
    "Atwima Kwanwoma",
    "Atwima Mponua",
    "Bawku",
    "Birim South",
    "Bodi",
    "Bole",
    "Dormaa East",
    "Ga Central",
    "Ga East",
    "Kwahu South",
    "Kwahu West",
    "La Dade-Kotopon",
    "La Nkwantanang Madina",
    "Lambussie Karni",
    "Lawra",
    "Mion",
    "Nkoranza South",
    "Nkwanta North",
    "Offinso",
    "Pusiga",
    "Tano South",
    "Weija Gbawe",
    "Wenchi",
]

accra = [
    "Entire Region",
    "Ablekuma Central",
    "Ablekuma North",
    "Ablekuma West",
    "Achiase",
    "Ada West",
    "Adaklu",
    "Afadzato South",
    "Asokore Mampong",
    "Ayawaso North",
    "Ayawaso West",
    "Ayensuano",
    "Banda",
    "Ga North",
    "Ga South",
    "Ga West",
    "Garu",
    "Gomoa Central",
    "Kpone Katamanso",
    "Krachi West",
    "Kwadaso",
    "Ledzokuku",
    "Lower Manya Krobo",
    "Mfantsiman",
    "Nkwanta South",
    "Pru West",
    " Suaman",
    "Upper Manya Krobo",
    "Zabzugu",
]

ne = [
    "Entire Region",
    "Central Gonja",
    "Effutu",
    "Nabdam",
]

north = [
    "Entire Region",
    "Denkyembuor",
    "Ho West",
    "Keta",
    "Krachi East",
    "Kwahu Afram Plains North",
    "Nandom",
    "New Juaben South",
    "Ningo Prampram",
    "Nkoranza North",
    "Sefwi Wiawso",
    "Sekyere Afram Plains",
    "Sekyere Central",
    "Tema West",
    "Twifo Heman Lower Denkyira",
    "Wa",
]

oti = [
    "Entire Region",
    "Binduri",
    "Juaben",
    "Kasena Nankana West",
    "Krowor",
    "Kumbungu",
    "Kwabre East",
    "North Gonja",
    "North Tongu",
]

sav = [
    "Entire Region",
    "Bolgatanga",
    "Chereponi",
    "Effia Kwesimintsim",
    "Nzema East",
    "Offinso North",
    "Sekyere East",
]

ue = [
    "Entire Region",
    "Bekwai",
    "Berekum East",
    "Birim North",
    "Bongo",
    "Bosome Freho",
    "Bosomtwe",
    "Bunkpurugu Nakpanduri",
    "Cape Coast Metro",
    "Gomoa East",
    "Ketu North",
    "Ketu South",
    "Nanumba North",
    "Sefwi Akontombra",
    "Techiman North",
    "Wa East",
]

uw = [
    "Entire Region",
    "Dormaa Central",
    "Juaboso",
    "Mampong",
    "Mamprugu Moagduri",
    "Nanumba South",
    "New Juaben North",
    "Suhum",
    "Sunyani",
    "West Akim",
    "West Gonja",
    "West Mamprusi",
]

volta = [
    "Entire Region",
    "Adansi Asokwa",
    "Afigya Kwabre North",
    "Ahafo Ano North",
    "Akatsi South",
    "Akrofuom",
    "Asante Akim Central",
    "Daffiama Bussie Issa",
    "Hohoe",
    "Jaman North",
    "Jaman South",
    "Kintampo North",
    "Kintampo South",
    "Komenda Edina Eguafo Abirem",
    "Krachi Nchumuru",
    "Nsawam Adoagyiri",
    "Obuasi East",
    "Sunyani West",
    "Tain",
]

western = [
    "Entire Region",
    "Ajumako Enyan Essiam",
    "Aowin",
    "Ejisu",
    "Fanteakwa South",
    "Kadjebi",
    "Nanton",
    "Oforikrom",
    "Sagnarigu",
    "Sene East",
    "Suame",
    "Twifo Ati Morkwa",
    "Yendi",
    "Yilo Krobo",
    "Yunyoo Nasuan",
]

west_north = [
    "Entire Region",
    "Asante Akim North",
    "Biakoye",
    "Bibiani Anhwiaso Bekwai",
    "Birim Central",
    "Bolgatanga East",
    "Kasena Nankana",
    "Sekyere Kumawu",
    "Sekyere South",
    "Talensi",
]

yr_selectable = [
    "2020",
    "2025",
    "2030",
    "2035",
    "2040",
    "2045",
    "2050",
    "2055",
    "2060",
    "2065",
    "2070",
    "2075",
    "2080",
    "2085",
    "2090",
    "2095",
    "2100",
]