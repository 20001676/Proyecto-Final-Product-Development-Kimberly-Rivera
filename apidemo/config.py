#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = []

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = []

#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Income']

#Variables para binarización por sesgo fuerte
BINARIZE_VARS = ['MntFruits', 'MntSweetProducts', 'MntFishProducts', 'MntMeatProducts','MntWines','MntGoldProds']

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = ['Education', 'Marital_Status']

#Variables seleccionadas según análisis de Lasso
FEATURES = [
    'Education', 
    'Marital_Status',
    'ID',
    #'Year_Birth',
    'Income',
    'Kidhome',
    'Teenhome',
    'Recency',
    'MntWines',
    'MntFruits',
    'MntMeatProducts',
    'MntFishProducts',
    'MntSweetProducts',
    'MntGoldProds',
    'NumDealsPurchases',
    'NumCatalogPurchases',
    'NumStorePurchases',
    'NumWebVisitsMonth',
    'AcceptedCmp3',
    'AcceptedCmp4',
    'AcceptedCmp5',
    'AcceptedCmp1',
    'AcceptedCmp2',
    'Complain',
    'Z_CostContact',
    'Z_Revenue',
    'Response',
    #'dia',
    #'mes',
    #'Year',
]