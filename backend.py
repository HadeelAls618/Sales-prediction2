
# backend-related code here

def prediction(ItemFatContent,OutletSize,ItemType,ItemWeight,ItemMRP):

#2-map the categorical variebles to numerical


  # 2. Loading and Pre-processing the data

    if ItemFatContent == "Low Fat":
        ItemFatContent = 0
    else:
        ItemFatContent = 1

    if ItemType == "Dairy":
        ItemType = 0
    elif ItemType == "Drinks":
        ItemType = 1
    elif ItemType == "Fruits":
        ItemType = 2
    else:
        ItemType = 3

    if OutletSize == "Small":
        OutletSize = 0
    elif OutletSize == "Medium":
        OutletSize = 1
    else:
        OutletSize = 2


    prediction=Regrissor.predict([[ItemFatContent,OutletSize,ItemType,ItemWeight,ItemMRP]])
    print(prediction)
    return prediction


if __name__=='__main__':
    main()

